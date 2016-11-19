# mongo.py
import os

from flask import Flask
from flask import jsonify
from flask import request
# from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
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
@app.route('/star', methods=['GET'])
def get_all_stars():
    # games = mongo.db.games
    games = db.games
    output = []
    for s in games.find({}):
        s.pop('_id')
        # output.append({'name' : s['name'], 'distance' : s['distance']})
        output.append(s)
    return jsonify({'result' : output})

# @app.route('/star/', methods=['GET'])
# def get_one_star(name):
#   star = mongo.db.stars
#   s = star.find_one({'name' : name})
#   if s:
#     output = {'name' : s['name'], 'distance' : s['distance']}
#   else:
#     output = "No such name"
#   return jsonify({'result' : output})

# @app.route('/star', methods=['POST'])
# def add_star():
#   star = mongo.db.stars
#   name = request.json['name']
#   distance = request.json['distance']
#   star_id = star.insert({'name': name, 'distance': distance})
#   new_star = star.find_one({'_id': star_id })
#   output = {'name' : new_star['name'], 'distance' : new_star['distance']}
#   return jsonify({'result' : output})

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
