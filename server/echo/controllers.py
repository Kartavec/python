from protocol import make_response
from decorators import logger_required, login_required

@logger_required
@login_required
def get_echo(request):
    data = request.get('data')
    return make_response(request, 200, data)


#компрессия и декомпрессия данных

