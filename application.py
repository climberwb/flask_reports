from flask import Flask
import os
# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    
'''
    {
        attempts:
            {
                        #maybe total levels in game,
                        attempts:{
                            [
                                {   ###gameId,
                                    userId, 
                                    Level,
                                    time, 
                                    timestamp, 
                                    incorrect,# #of explosions 
                                    correct,  # number of correct pairs in this case max is one,
                                    totalPossibleCorrect, # in this case one
                                    completedAttempt,
                                    gameInLevel: #this is for keeping track if there are multiple game attempts in a level. 
                                },
                                
                            ]
                        }
                    }

    }
    
    query to mlabs https://api.mlab.com/api/1/databases/attempts/collections/attempts/?q={%22level%22:1}&apiKey=u8YtBzwVyloYLy6hBUdgeLjOz1tygzUx
'''