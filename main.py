import requests
from flask import Flask, render_template,url_for,redirect,request
import smtplib


post_url = "https://api.npoint.io/9b8320f489af05d1cacb"
posts = requests.get(post_url).json()

my_mail = "freethinkernyc@gmail.com"
password = "pydrfpzhqsvsnojb"

app = Flask(__name__)


@app.route("/")
def get_posts():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    request_post = None
    for post in posts:
        if post["id"] == index:
            request_post = post
    return render_template("post.html", post=request_post)


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method=="POST":
        data=request.form
        email_message=f"Subject:New Message\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage:{data['message']}"

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs="chloe_619@yahoo.com",
                                msg=email_message)
        return render_template("contact.html",msg_sent=True)
    return render_template("contact.html",msg_sent=False)



if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0') for phone
    app.run(debug=True, host='localhost', port=5000)
