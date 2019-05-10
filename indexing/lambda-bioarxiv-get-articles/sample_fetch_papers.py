"""
Queries arxiv API and downloads papers (the query is a parameter).
The script is intended to enrich an existing database pickle (by default db.p),
so this file will be loaded first, and then new results will be added to it.
"""

import os
import time
import pickle
import random
import argparse
import urllib.request
import feedparser

from utils import Config, safe_pickle_dump, parse_biorxiv_url, \
                  biorxiv_categories, biorxiv_hacks


def encode_feedparser_dict(d):
    """
    helper function to get rid of feedparser bs with a deep copy.
    I hate when libs wrap simple things in their own classes.
    """
    if isinstance(d, feedparser.FeedParserDict) or isinstance(d, dict):
        j = {}
        for k in d.keys():
            j[k] = encode_feedparser_dict(d[k])
        return j
    elif isinstance(d, list):
        l = []
        for k in d:
            l.append(encode_feedparser_dict(k))
        return l
    else:
        return d


def parse_arxiv_url(url):
    """
    examples is http://arxiv.org/abs/1512.08756v2
    we want to extract the raw id and the version
    """
    # strip off ?rss=1 if it exists
    url = url[:url.rfind('?') if '?' in url else None]
    ix = url.rfind('/')
    idversion = url[ix+1:]  # extract just the id (and the version)
    parts = idversion.split('v')
    assert len(parts) == 2, 'error parsing url ' + url
    return parts[0], int(parts[1])


if __name__ == "__main__":
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--search_query', type=str, default='everything', help='bioRxiv category to download e.g. genomics+bioinformatics')
    parser.add_argument('--wait-time', type=float, default=1.0, help='lets be gentle to biorxiv (in number of seconds)')
    args = parser.parse_args()
    # misc hardcoded variables
    base_url = 'http://connect.biorxiv.org/biorxiv_xml.php?'
    print('Searching bioRxiv for %s' % (args.search_query, ))

    # lets load the existing database to memory
    try:
        db = pickle.load(open(Config.db_path, 'rb'))
    except Exception as e:
        print('error loading existing database:')
        print(e)
        print('starting from an empty database')
        db = {}

    # -----------------------------------------------------------------------------
    # main loop where we fetch the new results
    print('database has %d entries at start' % (len(db), ))
    num_added_total = 0

    if (args.search_query == 'everything'):
        cats = [x.lower().replace(' ', '_') for x in biorxiv_categories]
    else:
        cats = args.search_query.split('+')

    for cat in cats:
        print("Downloading %s..." % cat)
        query = 'subject=%s' % cat
        with urllib.request.urlopen(base_url+query) as url:
            response = url.read()
        parse = feedparser.parse(response)
        num_added = 0
        num_skipped = 0
        for e in parse.entries:
            j = encode_feedparser_dict(e)

        # extract just the raw arxiv id and version for this paper
        rawid, version = parse_biorxiv_url(j['id'])
        j['_rawid'] = rawid
        j['_version'] = version

        # add to our database if we didn't have it before, or if this is a new version
        if (j['_rawid'] is not None and j['_version'] is not None) and \
           (rawid not in db or j['_version'] > db[rawid]['_version']):
            db[rawid] = biorxiv_hacks(j, cat)
            print('Updated %s added %s' % (j['updated'].encode('utf-8'), j['title'].encode('utf-8')))
            num_added += 1
            num_added_total += 1
        else:
            num_skipped += 1

        # print some information
        print('Added %d papers, already had %d.' % (num_added, num_skipped))

        if len(parse.entries) == 0:
            print('Received no results from bioRxiv. Rate limiting? Exiting. Restart later maybe.')
            print(response)
            break

        print('Sleeping for %i seconds' % (args.wait_time, ))
        time.sleep(args.wait_time + random.uniform(0, 3))

    # save the database before we quit, if we found anything new
    if num_added_total > 0:
        print('Saving database with %d papers to %s' % (len(db), Config.db_path))
        safe_pickle_dump(db, Config.db_path)
