# Indexing Pubmed data

Pull data from Pubmed Central (the Open Access papers)


## Resources

* https://www.ncbi.nlm.nih.gov/home/develop/api/
* https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
* http://www.fredtrotter.com/2014/11/14/hacking-on-the-pubmed-api/
* https://gist.github.com/briatte/542736520e8b42e6a08e
* https://stackoverflow.com/questions/26899053/download-all-pubmed-abstracts
* https://www.biostars.org/p/10026/ <- very useful
* https://support.ncbi.nlm.nih.gov/link/portal/28045/28049/Article/717/What-are-NCBI-s-guidelines-for-high-frequency-retrievals-using-NCBI-web-services
* https://www.ncbi.nlm.nih.gov/books/NBK25497/#chapter2.Usage_Guidelines_and_Requiremen


## Resources

* [Arxiv Sanity Preserver](https://github.com/karpathy/arxiv-sanity-preserver) - the original idea for this
* [A quick bioarxiv scrape](http://predictablynoisy.com/scrape-biorxiv.html)
* [Prepubmed monthly stats](http://www.prepubmed.org/monthly_stats/)
	* [Bioarxiv Prepub](https://github.com/OmnesRes/prepub/blob/master/biorxiv/biorxiv.py)
* [A Twitter bot to find the most interesting bioRxiv preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/)

### Flask and Serverless

* http://blog.apcelent.com/deploy-flask-aws-lambda.html
* https://hackernoon.com/deploy-a-serverless-flask-application-on-aws-lambda-d8ca58af42a4

* Lambda, Python + dynamodb, https://stackoverflow.com/questions/33535613/how-to-put-an-item-in-aws-dynamodb-using-aws-lambda-with-python 
* https://micropyramid.com/blog/using-aws-lambda-with-s3-and-dynamodb/
* http://tech.adroll.com/blog/dev/2015/11/16/count-things-with-aws-lambda-python-and-dynamodb.html


### Ingestion

* Use the per-date search, https://www.biorxiv.org/search/limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed 
	* Too big

* Try a 7-day per-collection search, i.e. https://www.biorxiv.org/search/subject_collection_code%3ABioinformatics%20limit_from%3A2018-04-01%20limit_to%3A2018-04-26%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed

### Storage

* DynamoDB, https://aws.amazon.com/dynamodb/pricing/
* https://aws.amazon.com/dynamodb/getting-started/
* https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html


### Analysis

# VM Design

* Pull everything
* Save articles to pull to file (in S3?)
* Save all PDFs to S3
* Convert all PDFs to text, save to S3
* Run Analysis
* Save results to S3

# Serverless Design

* A cron job (Cloudwatch) fires off once a day, a bit after midnight, when bioarxiv updates. It stores one record per day and topic into an SQS queue, Bioarxiv-DayAndChannelQueue, via SNS
* A SNS watcher (?) on the Bioarxiv-DayAndChannelQueue fires onto a Lambda function, Bioarxiv-GetArticleIdFromDayAndChannel
	* Set a concurrency limit on this of 4 to avoid slamming the bioarxiv server, https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
* The Bioarxiv-GetArticleIdFromDayAndChannel takes a channel & date as input and gets all the articles for that day. It then saves those off to another SQS queue, Bioarxiv-ArticlesToPull
* The Bioarxiv-ArticlesToPull queue fires off a Lambda function via SNS, BioArxiv-GetArticleById
* The BioArxiv-GetArticleById Lambda function takes an ID as input, downloads the PDF, converts it to text, and saves the text file 

* Get each article, 


* The Bioarxiv-AnalyzeTFIDF EC2 instance starts. It's a spot instance
	* It [runs a script on startup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
	* 



*Misc*

* Use [dead letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) for commands with errors


# Serverless Website Design

* All state is stored in <>
* Lambda functions are used to serve the site




# Steps

* DONE: Find some useful resources
* Go through my old resources, copy them in
* DONE: Make GitHub repo
* Set up AWS on laptop
* Make 'hello world' lambda function w/ Flask
* 




