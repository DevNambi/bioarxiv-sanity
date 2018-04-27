# Indexing the Bioarxiv

This is the initial version of indexing the Bioarxiv, which focuses on doing it all in a single VM, as a single batch process.

## Resources

* [Arxiv Sanity Preserver](https://github.com/karpathy/arxiv-sanity-preserver) - the original idea for this
* [A quick bioarxiv scrape](http://predictablynoisy.com/scrape-biorxiv.html)
* [Prepubmed monthly stats](http://www.prepubmed.org/monthly_stats/)
	* [Bioarxiv Prepub](https://github.com/OmnesRes/prepub/blob/master/biorxiv/biorxiv.py)
* [A Twitter bot to find the most interesting bioRxiv preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/)


### Ingestion

* Use the per-date search, https://www.biorxiv.org/search/limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed 
	* Too big

* Try a 7-day per-collection search, i.e. https://www.biorxiv.org/search/subject_collection_code%3ABioinformatics%20limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed


### Analysis

# VM Design

* Pull everything
* Save articles to pull to file (in S3?)
* Save all PDFs to S3
* Convert all PDFs to text, save to S3
* Run Analysis
* Save results to S3






# Steps

* DONE: Find some useful resources
* Go through my old resources, copy them in
* DONE: Make GitHub repo
* Set up AWS on laptop
* Make 'hello world' lambda function w/ Flask
* 




