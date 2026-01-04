from flask import Flask
'''
create an instance of the flask class,
which will be your WSGI(Webserver Gateway Interface) application
'''
### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. This should be an amazing course.p"

@app.route("/index")
def index():
    return "Lets learn ML"

if __name__=="__main__":
    app.run(debug=True)