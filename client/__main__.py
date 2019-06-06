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
try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client started')
    data = input('Enter data: ')
    sock.send(data.encode(encoding))
    response = sock.recv(buffersize)
    print(response.decode(encoding))
except KeyboardInterrupt:
    pass