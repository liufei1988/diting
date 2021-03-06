#-*-coding: utf-8-*-

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from web_ditingai_cn import app
import time



import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main1():
    app.run(host='0.0.0.0', port=6100, threaded=True, debug=True)

def main2():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(6100)
    print '-------- successful startup -------'
    IOLoop.instance().start()

app.config['SESSION_TYPE'] = 'filesystem'
app.config['APIURL'] = '/api'

if __name__ == "__main__":
    main2()