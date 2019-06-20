#!/usr/local/bin/python

import yaml
import socket
import json
import logging
import select
from argparse import ArgumentParser
from handlers import handle_default_request
from actions import resolve
from protocol import validate_request, make_response

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file')

args = parser.parse_args()

host = '0.0.0.0' #'localhost'
port = 8000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader = yaml.Loader)
        host = config.get('host')
        port = config.get('port')

# logger = logging.getLogger('main)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('main.log') #encoding
#
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.DEBUG)
#
# logger.addHandler(file_handler)
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log', encoding=encoding),
        logging.StreamHandler()
    ])

# print(f'Client run on {host}:{port}')
# data = input('Enter data: ')
# print(data)

connections = []
requests = []

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.setblocking(False)
    sock.listen(5)
    logging.info(f'Server was started on {host}:{port}')

    while True:
        try:
            client, address = sock.accept()
            logging.info(f'client with address {address} was detected')
            connections.append(client)
        except:
            pass
        rlist, wlist, xlist = select.select(connections, connections, connections, 0)

        for r_client in rlist:
            b_request = client.recv(buffersize)
            requests.append(b_request)

        if requests:
            b_request = requests.pop() #последний элемент
            b_response = handle_default_request(b_request)
            for w_client in wlist:
                w_client.send(b_response)

except KeyboardInterrupt:
    pass

