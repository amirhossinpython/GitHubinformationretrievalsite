from flask import Flask, render_template, request  
import requests  

app = Flask(__name__)  

def is_valid_github_username(username):  
    url = f"https://api.github.com/users/{username}"  
    response = requests.get(url)  
    return response.status_code == 200  

def get_github_user_info(username):  
    url = f"https://api.github.com/users/{username}"  
    response = requests.get(url)  

    if response.status_code == 200:  
        return response.json()    
    else:  
        return None   

def display_user_info(user_info):  
    if user_info:  
        print("جزئیات کاربر GitHub:\n")  
        print(f"نام کاربری: {user_info['login']}")  
        print(f"شناسه کاربر: {user_info['id']}")  
        print(f"آدرس پروفایل: {user_info['html_url']}")  
        print(f"تصویر پروفایل: {user_info['avatar_url']}")  
        print(f"تعداد دنبال‌کنندگان: {user_info['followers']}")  
        print(f"تعداد دنبال‌شوندگان: {user_info['following']}")  
        print(f"تعداد ریپوزیتوری‌های عمومی: {user_info['public_repos']}")  
        print(f"تاریخ عضویت: {user_info['created_at']}")  
        print(f"بیوگرافی: {user_info['bio'] if user_info['bio'] else 'ندارد'}")  
    else:  
        print("❌ نام کاربری GitHub معتبر نیست!")  

@app.route("/", methods=["GET", "POST"])  
def index():  
    user_info = None  
    if request.method == "POST":  
        username = request.form.get("username").strip()  
        if is_valid_github_username(username):  
            user_info = get_github_user_info(username)  
            if user_info:  
                stats_url = f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&count_private=true&theme=radical"  
                languages_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=radical"  
                animation_url = f"https://raw.githubusercontent.com/imrrobat/imrrobat/d1b244e170d2b75fdda3efd499eaaf163f7a617c/images/github-contribution-grid-snake.svg"  
                
                
                display_user_info(user_info)  
                
                return render_template("stats.html", username=username, stats_url=stats_url, languages_url=languages_url, animation_url=animation_url, user_info=user_info)  
            else:  
                return render_template("index.html", error="❌ مشکلی در دریافت اطلاعات کاربر پیش آمد.")  
        else:  
            return render_template("index.html", error="❌ شناسه GitHub معتبر نیست!")  
    return render_template("index.html")  

if __name__ == "__main__":  
    app.run(debug=True)  
