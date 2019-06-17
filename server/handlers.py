import json
import logging
from actions import resolve
from protocol import validate_request, make_response
from middlewares import compression_middlware

@compression_middlware
def handle_default_request(raw_request):
    request = json.loads(
        raw_request.decode()
    )

    if validate_request(request):
        action_name = request.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                response = controller(request)
            except Exception as err:
                logging.critical(err)
                response = make_response(request, 500, 'Internal server error')
        else:
            logging.error(f'404 - request: {request}')
            response = make_response(request, 404, 'Action not found')
    else:
        logging.error(f'400 - request: {request}')
        response = make_response(request, 400, 'Wrong request')

    return json.dumps(response).encode()



