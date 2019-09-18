import spacy
import json

ERROR_MSG = 'Please ensure that the `text` parameter is being passed'
EMPTY_MSG = 'No people were detected from the text provided.'


def main(event, context):
    if 'isOffline' in event:
        # All Lambda layers are accessible within the /opt/ directory.
        nlp = spacy.load('en_core_web_sm-2.1.0')
    else:
        nlp = spacy.load('/opt/en_core_web_sm-2.1.0')

    # Return early to minimise resource usage if invoked by warmup plugin
    if event.get('source') in ['aws.events', 'serverless-plugin-warmup']:
        print('Keeping the Lambda warm...')
        return {}

    def get_names(text_):
        doc = nlp(text_)
        entities_ = []

        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                entity = {
                    'person': ent.text,
                }
                entities_.append(entity)
        return entities_

    try:
        text = event['queryStringParameters']['text']
    except (TypeError, KeyError):
        text = ERROR_MSG

    if text is not ERROR_MSG:
        entities = get_names(text)
        if not entities:
            entities = [{
                'empty': EMPTY_MSG
            }]
    else:
        entities = [{
            'error': ERROR_MSG
        }]

    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(entities)
    }

    return response
