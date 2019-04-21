# -*- coding: utf-8 -*-
#########################################################
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugin'))
# 반드시 필요. websocket. 없는 경우 ping_interval 주기로만 통신함. thread=false 넣으면 안됨.
try:
    from gevent import monkey;monkey.patch_all()
except:
    print 'not monkey'

import framework
import system

app = framework.app
#celery = framework.celery
#socketio = framework.socketio
 
"""
try:
    from ddtrace import patch_all
    patch_all()
except:
    pass
"""

def start_app(port=None):
    if port is None: 
        try :
            entity = framework.db.session.query(system.model.ModelSetting).filter_by(key='port').first()
            if entity is not None:
                port = int(entity.value)
        except:
            print 'port is none.'
    try:
        framework.socketio.run(app, host='0.0.0.0', port=port)
    except Exception as e:
        print e

if __name__ == '__main__':
    try:
        #import multiprocessing
        #multiprocessing.set_start_method('spawn')
        port = None
        if len(sys.argv) > 1:
            port = int(sys.argv[1])

        start_app(port)
        #, async_mode='greenlet')
        #app.run(host='0.0.0.0', port=9997, debug=False)
        #from gevent.pywsgi import WSGIServer
        #print 'WSGIServer start..'
        #http = WSGIServer(('0.0.0.0', 9997), app.wsgi_app)
        #http.serve_forever()
    except Exception as e:
        print e
        
