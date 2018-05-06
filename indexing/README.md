# Indexing the Bioarxiv

This is the initial version of indexing the Bioarxiv, which focuses on doing it all in a single VM, as a single batch process.

## Resources

* [Arxiv Sanity Preserver](https://github.com/karpathy/arxiv-sanity-preserver) - the original idea for this
* [A quick bioarxiv scrape](http://predictablynoisy.com/scrape-biorxiv.html)
* [Prepubmed monthly stats](http://www.prepubmed.org/monthly_stats/)
	* [Bioarxiv Prepub](https://github.com/OmnesRes/prepub/blob/master/biorxiv/biorxiv.py)
* [A Twitter bot to find the most interesting bioRxiv preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/)


### Ingestion

**Get Collections**

100 results, 2018-01-01 to 2018-05-01

Animal Behavior and Cognition - https://www.biorxiv.org/search/subject_collection_code%3AAnimal%20Behavior%20and%20Cognition%20limit_from%3A2018-01-01%20limit_to%3A2018-05-01%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Biochemistry - https://www.biorxiv.org/search/subject_collection_code%3ABiochemistry%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Bioengineering - https://www.biorxiv.org/search/subject_collection_code%3ABioengineering%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Bioinformatics - https://www.biorxiv.org/search/subject_collection_code%3ABioinformatics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Biophysics - https://www.biorxiv.org/search/subject_collection_code%3ABiophysics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Cancer Biology - https://www.biorxiv.org/search/subject_collection_code%3ACancer%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Cell Biology - https://www.biorxiv.org/search/subject_collection_code%3ACell%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Clinical Trials - https://www.biorxiv.org/search/subject_collection_code%3AClinical%20Trials%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Developmental Biology - https://www.biorxiv.org/search/subject_collection_code%3ADevelopmental%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Ecology - https://www.biorxiv.org/search/subject_collection_code%3AEcology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Epidemiology - https://www.biorxiv.org/search/subject_collection_code%3AEpidemiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Evolutionary Biology - https://www.biorxiv.org/search/subject_collection_code%3AEvolutionary%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Genetics - https://www.biorxiv.org/search/subject_collection_code%3AGenetics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Genomics - https://www.biorxiv.org/search/subject_collection_code%3AGenomics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Immunology - https://www.biorxiv.org/search/subject_collection_code%3AImmunology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Microbiology - https://www.biorxiv.org/search/subject_collection_code%3AMicrobiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Molecular Biology - https://www.biorxiv.org/search/subject_collection_code%3AMolecular%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Neuroscience - https://www.biorxiv.org/search/subject_collection_code%3ANeuroscience%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Paleontology - https://www.biorxiv.org/search/subject_collection_code%3APaleontology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Pathology - https://www.biorxiv.org/search/subject_collection_code%3APathology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Pharmacology and Toxicology - https://www.biorxiv.org/search/subject_collection_code%3APharmacology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Physiology - https://www.biorxiv.org/search/subject_collection_code%3APhysiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Plant Biology - https://www.biorxiv.org/search/subject_collection_code%3APlant%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Scientific Communication and Education - https://www.biorxiv.org/search/subject_collection_code%3AScientific%20Communication%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Synthetic Biology - https://www.biorxiv.org/search/subject_collection_code%3ASynthetic%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Systems Biology - https://www.biorxiv.org/search/subject_collection_code%3ASystems%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

Zoology - https://www.biorxiv.org/search/subject_collection_code%3AZoology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed





**Generate Dates and Collections into SQS Queue**

* Boto Docs - http://boto.readthedocs.io/en/latest/sqs_tut.html

* Do a 1 day search per collection
* Generate dates and collections, store them into an SQS queue, https://sqs.us-west-2.amazonaws.com/778552047182/bioarxiv-sanity-dates 

**Parse a search result into a list of articles and DOIs**

* Use the per-date search, https://www.biorxiv.org/search/limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed 
   * Too big

* Try a 7-day per-collection search, i.e. https://www.biorxiv.org/search/subject_collection_code%3ABioinformatics%20limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

**Iterate over an SQS queue, get articles, store into another SQS queue**

* Generate articles to pull, store them in an SQS queue, https://sqs.us-west-2.amazonaws.com/778552047182/bioarxiv-sanity-articles-to-pull   


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




