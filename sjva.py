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
# update:1
# restart:2

def start_app():
    try:
        framework.socketio.run(app, host='0.0.0.0', port=app.config['config']['port'])
        print 'EXIT CODE : %s' % framework.exit_code
        if framework.exit_code != -1:
            sys.exit(framework.exit_code)
    except Exception as e:
        print e
    except KeyboardInterrupt:
        print 'KeyboardInterrupt !!'

if __name__ == '__main__':
    try:
        start_app()
    except Exception as e:
        print e
        
