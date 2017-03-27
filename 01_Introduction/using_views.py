import bottle


@bottle.route('/')
def index():
    things = [1,2,3]
    return bottle.template('index', {'name':'V G', 'things':things})

@bottle.post('/fav_fruit')
def fav_fruit():
    fruit = bottle.request.forms.get("fruit")
    if fruit == None or fruit == '':
        fruit = 'fruit not selected'
    bottle.response.set_cookie('fruit', fruit);
    bottle.redirect('/show_fruit')

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie('fruit')
    return bottle.template('fruit_selected', {'fruit': fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8080)