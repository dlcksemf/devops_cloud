from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    # DB Access
    like_foods = ["젤리", "만두", "짜장면", "아이스크림", "탕수육"]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
