from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def is_valid_github_username(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.status_code == 200

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username").strip()
        if is_valid_github_username(username):
            stats_url = f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&count_private=true&theme=radical"
            languages_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=radical"
            animation_url = f"https://raw.githubusercontent.com/imrrobat/imrrobat/d1b244e170d2b75fdda3efd499eaaf163f7a617c/images/github-contribution-grid-snake.svg"
            return render_template("stats.html", username=username, stats_url=stats_url, languages_url=languages_url, animation_url=animation_url)
        else:
            return render_template("index.html", error="❌ شناسه GitHub معتبر نیست!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)