from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# @app.route("/user")
# def username():
#     return render_template("index.html", name = 'yaacov', color = "green", background_color = "red")

users = [
    {"name":"yaacov", "email":"yaacov@gmail.com"},
    {"name": "yossef", "email": "yossef@gmail.com"},
    {"name": "batsi", "email": "batsi@gmail.com"}
]

@app.route("/")
def pages_colors():
    # return render_template("link_colors.html")
    return name_mails()


@app.route("/color/<chosen_color>")
def color(chosen_color):
    return render_template("color.html", background_color=chosen_color)


@app.route("/names")
def names():
    return render_template("names.html")


@app.route("/name_mails")
def name_mails():
    return render_template("name_mails.html", users = users)

if __name__ == "__main__":
    app.run(debug= True)