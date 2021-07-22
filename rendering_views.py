from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<phrase>/<int:times>")
def index(phrase, times):
    return render_template("rendering.html", phrase = phrase, times = times)

if __name__ == "__main__":
    app.run(debug=True)