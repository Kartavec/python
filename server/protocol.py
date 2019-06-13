from datetime import datetime

def validate_request(raw):
    if 'time' in raw and 'action' in raw:
        return True
    return False

def make_response(request, code, data=None):
    return{
        'action': request.get('action'),
        'user': request.get('user'),
        'time': datetime.now().timestamp(),
        'data': data,
        'code': code
    }



