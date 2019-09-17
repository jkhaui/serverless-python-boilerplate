import json

ERROR_MSG = 'Error: Please ensure that the `text` parameter is ' \
            'being passed'


def main(event, context):
    """
    The main handler function called when the Lambda function is invoked.
     Arguments:
         event {dict} -- Dictionary containing contents of the event that
         invoked the function, primarily the payload of data to be processed.
         context {LambdaContext} -- An object containing metadata describing
         the event source and client details.
     Returns:
         [string|dict] -- An output object that does not impact the effect of
         the function but which is reflected in CloudWatch
     """
    try:
        query_string = event['queryStringParameters']['text']
    except TypeError:
        query_string = ERROR_MSG

    body = {
        'result': query_string
    }

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(body)
    }

    return response
