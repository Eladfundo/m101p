import bottle

@bottle.route('/')
def home_page():
    return "Hello world!\n";

@bottle.route('/test')
def test_page():
    return 'This is a test page'

bottle.debug(True)
bottle.run(host='localhost', port=8080)