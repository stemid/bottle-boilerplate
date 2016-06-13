# Boilerplate code for bottle.py apps

# Makes debugging easier
from pprint import pprint

# Until pyvenv-3.4 is fixed on centos 7 support python 2.
try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser

from bottle import default_app, route, run
from bottle import request, response, template, static_file

# If we need custom filters
#from bottle import Bottle
#app = Bottle()
#app.router.add_filter('uuid', uuid_filter)
# Also must use app.route() instead of just route as decorator.

## Custom UUID route filter for bottle.py
#def uuid_filter(config):
#    # Should catch UUIDv4 type strings
#    regexp = r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}'
#
#    def to_python(match):
#        return UUID(match, version=4)
#
#    def to_url(uuid):
#        return str(uuid)
#
#    return regexp, to_python, to_url

# End of custom filters


config = RawConfigParser()
config.readfp(open('./app.cfg'))


# Serve static files
@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root=config.get('app', 'static_dir'))


@route('/')
def index():
    return template('index')


if __name__ == '__main__':
    run(
        host=config.get('app', 'listen_host'),
        port=config.getint('app', 'listen_port')
    )
    debug(config.getbool('app', 'debug'))
else:
    application = default_app
