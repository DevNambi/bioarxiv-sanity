# Indexing the Bioarxiv

This is the future (V2) version of this indexing process, which uses serverless techniques.


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

