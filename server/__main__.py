#!/usr/local/bin/python

import yaml
import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file')

args = parser.parse_args()

host = 'localhost'
port = 8000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader = yaml.Loader)
        host = config.get('host')
        port = config.get('port')

print(f'Client run on {host}:{port}')
data = input('Enter data: ')
print(data)

try:
    sock = socket.socket()

    sock.bind((host, port))
    sock.listen(5)
    print(f'Server was started with {host}:{port}')
    while True:
        client, address = sock.accept()
        print(f'Client was detected {address}')
        data = client.recv(buffersize)
        print(data.decode(encoding))
        client.send(data)
        client.close()
except KeyboardInterrupt:
    pass