from fabric.api import local

def server():
    local('python server')

def client():
    local('python client')

def test():
    local('python --cov-report term-missing --cov server')