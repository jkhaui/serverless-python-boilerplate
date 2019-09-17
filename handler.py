import spacy
import json

# All Lambda layers are accessible within the /opt/ directory.
nlp = spacy.load('/opt/en_core_web_sm-2.1.0')

ERROR_MSG = 'Error: Please ensure that the `text` parameter is ' \
            'being passed'


def main(event, context):
    def get_names(words):
        doc = nlp(words)
        names = []

        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                entity = {
                    'person': ent.text,
                }
                names.append(entity)
        return names

    try:
        text = event['queryStringParameters']['text']
    except TypeError:
        text = ERROR_MSG

    entities = None
    if text is not ERROR_MSG:
        entities = get_names(text)

    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(entities)
    }

    return response
