from flask import Flask

app = Flask(__name__) # app is an object or instance of flask

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/flask")
def say_flask():
    return "Hi Flask!"

@app.route("/say/michael")
def say_michael():
    return "Hi Michael!"

@app.route("/say/john")
def say_john():
    return "Hi John!"


@app.route("/repeat/35/hello")
def repeat_hello():       
    return "hello " * 35
@app.route("/repeat/80/bye")
def repeat_bye():       
    return "bye " * 80
@app.route("/repeat/99/dogs")
def repeat_dogs():       
    return "dogs " * 99

@app.route("/repeat/<int:times>/<phrase>")
def repeat_num_phrase(times, phrase):
    return f"{phrase} " * times

@app.route("/<error_message>")
def error(error_message):
    return "Please try again"

if __name__ == "__main__":
    app.run(debug = True)