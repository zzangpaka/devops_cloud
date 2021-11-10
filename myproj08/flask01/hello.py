from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    my_self = ["김진아", "92.01.30", "대전광역시"]
    like_foods = ["돼지고기 김치찌개", "회전초밥", "쌀국수"]
    return render_template("profile.html", like_foods=like_foods, my_self=my_self)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
