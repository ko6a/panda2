import os
import redis

from flask import Flask

app = Flask(__name__, static_url_path='')

r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/')
def pnda_main():
    return "counter:" + incr_redis()


def incr_redis():
    try:
        counter_now = r.get('counter_py')
        if counter_now:
            counter_now = (int(counter_now) + 1)
            r.set('counter_py', counter_now)
            print "counter_now:", counter_now
            print "r.get('counter_py')", r.get('counter_py')
            return r.get('counter_py')
        else:
            r.set('counter_py', 1)
            print 2
            return r.get('counter_py')
    except Exception, e:
        str(e)
        r.set('counter_py', 1)
        print 3
        return r.get('counter_py')


if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8082)))
    # app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))
