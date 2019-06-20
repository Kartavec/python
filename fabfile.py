from fabric.api import local

def server():
    local('python server')

def client(mode='w'):
    local(f'python client -m {mode}')

def test():
    local('python --cov-report term-missing --cov server')

def notebook():
    local('jupyter notebook')