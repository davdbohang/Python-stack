from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/<int:box_num>")
# def play(box_num):
#     return render_template("play.html", box_num=3)

# @app.route("/play/<int:box_num>")
# def play(box_num):
#     return render_template("play.html", box_num=box_num)

@app.route("/play/<int:box_num>/<box_color>")
def play(box_num, box_color):
    return render_template("play.html", box_num=box_num, box_color=box_color)







if __name__ == "__main__":
    app.run(debug = True)