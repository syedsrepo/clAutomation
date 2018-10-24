from flask import Flask
from flask import Response

import socket
import os
import sys
import time

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    hostname = socket.gethostname()
    homedir = os.environ['HOME']
    retval = hostname + ' ' + homedir
    print retval
    time.sleep(.005)
    return Response(retval, status=200, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=sys.argv[1], debug=True)
