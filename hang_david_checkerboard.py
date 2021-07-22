from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("checkerboard.html")

@app.route("/<int:x>")
def rows(x):
    return render_template("checkerboard.html",x = x)

@app.route("/<int:x>/<int:y>")
def rows_cols(x, y):
    return render_template("checkerboard.html",x = x, y = y)

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def rows_cols_colors(x, y, color1, color2):
    return render_template("checkerboard.html",x = x, y = y, color1 = color1, color2 = color2)



if __name__ == "__main__":
    app.run(debug = True)