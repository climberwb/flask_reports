# mongo.py
import os

from flask import Flask
from flask import jsonify
from flask import request
# from flask_cors import CORS, cross_origin

# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
# CORS(app)
# tutorial
# client = MongoClient('mongodb://ImASmarty:12345@dbh44.mlab.com:27447')
client = pymongo.MongoClient('dbh44.mlab.com', 27447)
db = client['attempts']
db.authenticate('ImASmarty', '12345')

app.config['MONGO_DBNAME'] = 'attempts'
app.config['DB_USERNAME'] = 'ImASmarty'
app.config['DB_PASSWORD'] = '12345'
app.config['MONGO_URI'] = 'mongodb://ImASmarty:12345@dbh44.mlab.com:27447/attempts'

# mongo = PyMongo(app)
# mongo = client
# mongo.api.authenticate('ImASmarty', '12345')


@app.route('/games', methods=['GET'])
# @cross_origin()
def get_all_games():
    print'dfdf'
    # games = mongo.db.games
    games = db.games
    output = []
    for s in games.find({}):
        s.pop('_id')
        # output.append({'name' : s['name'], 'distance' : s['distance']})
        output.append(s)
    return jsonify({'result' : output})

@app.route('/games/<gameId>', methods=['GET'])
def get_one_star(gameId):
    print 'get it'
    game = db.games
    g = game.find_one({'gameId' : gameId})
    if g:
        g.pop('_id')
        output = g
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/game', methods=['POST'])
def add_star():
    games = db.games
    gameId = request.json['gameId']
    general_game_attributes = request.json['generalGameAttributes']
    specific_game_attributes = request.json['specificGameAttributes']
    game_id = games.insert({'gameId': gameId, \
                            'generalGameAttributes': general_game_attributes, \
                            'specificGameAttributes':specific_game_attributes
        
                            })
    new_game = games.find_one({'_id': game_id })
    new_game.pop('_id')
    new_game.pop('attempts')
    return jsonify({'result' : new_game})

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))












# from flask import Flask
# import os
# # print a nice greeting.
# def say_hello(username = "World"):
#     return '<p>Hello %s!!</p>\n' % username

# # some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'

# # EB looks for an 'application' callable by default.
# application = Flask(__name__)

# # add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

# # add a rule when the page is accessed with a name appended to the site
# # URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

# # run the app.
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     application.debug = True
#     application.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    
# '''
#     {
#         attempts:
#             {
#                         #maybe total levels in game,
#                         attempts:{
#                             [
#                                 {   ###gameId,
#                                     userId, 
#                                     Level,
#                                     time, 
#                                     timestamp, 
#                                     incorrect,# #of explosions 
#                                     correct,  # number of correct pairs in this case max is one,
#                                     totalPossibleCorrect, # in this case one
#                                     completedAttempt,
#                                     gameInLevel: #this is for keeping track if there are multiple game attempts in a level. 
#                                 },
                                
#                             ]
#                         }
#                     }

#     }
    
#     query to mlabs https://api.mlab.com/api/1/databases/attempts/collections/attempts/?q={%22level%22:1}&apiKey=u8YtBzwVyloYLy6hBUdgeLjOz1tygzUx
# '''