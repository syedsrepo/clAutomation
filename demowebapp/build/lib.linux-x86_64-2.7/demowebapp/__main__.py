from flask import Flask
from flask import Response

import logging
from logging.handlers import RotatingFileHandler

import socket
import os
import sys
import time

app = Flask(__name__)
logger=logging.getLogger('demowebapp')
logger.setLevel(logging.DEBUG)
handler=logging.handlers.RotatingFileHandler('/var/log/demowebapp.log',maxBytes=10000000, backupCount=4)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
@app.route('/index/get', methods=['GET'])
def index_get():
    retval = 'GET Request'
    logger.debug('GET request received ' + socket.gethostname())
    hostname = socket.gethostname()
    time.sleep(.005)
    logger.debug('GET request returning 200 response')
    return Response(retval, status=200, mimetype='text/plain')


@app.route('/index/post', methods=['POST'])
def index_post():
    retval = 'POST Request'
    logger.debug('POST request received ' + socket.gethostname())
    hostname = socket.gethostname()
    time.sleep(.005)
    logger.debug('POST request returning 200 response')
    return Response(retval, status=200, mimetype='text/plain')

def main():
    print("Main Function")
    app.run(host= '0.0.0.0', port=sys.argv[1], debug=True, threaded=True)

if __name__ == '__main__':
    main()
