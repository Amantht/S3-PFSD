#import Flask
from flask import Flask

# create an instance(app)
app=Flask(__name__)

#Normal Route
@app.route("/")

#define method
def sample():
    return "Welcome to flask"
#dynamic routing
@app.route("/<name>")
def sample2(name):
    return (f'Hello{name}')
if __name__=="__main__":
    app.run()