import json
import boto3

# bioarxiv-category-filler
# LOGIC:
# get list of categories. Send them to an SQS queue

var_queue_url = 'https://sqs.us-west-2.amazonaws.com/778552047182/bioarxiv-sanity-categories'

def create_categories():
    category_dict = {}
    category_dict['animal-behavior'] = 'https://www.biorxiv.org/search/subject_collection_code%3AAnimal%20Behavior%20and%20Cognition%20limit_from%3A2018-01-01%20limit_to%3A2018-05-01%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['biochemistry'] = 'https://www.biorxiv.org/search/subject_collection_code%3ABiochemistry%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['bioengineering'] = 'https://www.biorxiv.org/search/subject_collection_code%3ABioengineering%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['bioinformatics'] = 'https://www.biorxiv.org/search/subject_collection_code%3ABioinformatics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['biophysics'] = 'https://www.biorxiv.org/search/subject_collection_code%3ABiophysics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['cancer-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3ACancer%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['cell-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3ACell%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['clinical-trials'] = 'https://www.biorxiv.org/search/subject_collection_code%3AClinical%20Trials%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['developmental-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3ADevelopmental%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['ecology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AEcology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['epidemiology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AEpidemiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['evolutionary-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AEvolutionary%20Biology%20numresults%3A100%20sort%3Apublication-da'
    category_dict['genetics'] = 'https://www.biorxiv.org/search/subject_collection_code%3AGenetics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['genomics'] = 'https://www.biorxiv.org/search/subject_collection_code%3AGenomics%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['immunology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AImmunology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['microbiology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AMicrobiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['neuroscience'] = 'https://www.biorxiv.org/search/subject_collection_code%3ANeuroscience%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['paleontology'] = 'https://www.biorxiv.org/search/subject_collection_code%3APaleontology%20numresults%3A100%20sort%3Apublication-date%'
    category_dict['pathology'] = 'https://www.biorxiv.org/search/subject_collection_code%3APathology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['pharmacology-toxicology'] = 'https://www.biorxiv.org/search/subject_collection_code%3APharmacology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['physiology'] = 'https://www.biorxiv.org/search/subject_collection_code%3APhysiology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['plant-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3APlant%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['scientific-communication-education'] = 'https://www.biorxiv.org/search/subject_collection_code%3AScientific%20Communication%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['synthetic-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3ASynthetic%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['systems-biology'] = 'https://www.biorxiv.org/search/subject_collection_code%3ASystems%20Biology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    category_dict['zoology'] = 'https://www.biorxiv.org/search/subject_collection_code%3AZoology%20numresults%3A100%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Acondensed'
    return category_dict

def send_categories_to_q(aws_client, category_dict):
    responses = []
    for cat_key, cat_value in category_dict.items():
        message = json.dumps({cat_key:cat_value})
        response = aws_client.send_message(
            QueueUrl=var_queue_url,
            MessageBody=message
        )
        print('SQS response: {}'.format(response))
        responses.append(response)
    return responses

def lambda_handler(event, context):
    aws_client = boto3.client('sqs')
    categories = create_categories()
    sqs_responses = send_categories_to_q(aws_client, categories)
    return {
        'statusCode': 200,
        'body': json.dumps(sqs_responses)
    }
