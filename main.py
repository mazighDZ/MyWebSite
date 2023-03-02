from flask import Flask
from flask import render_template
from flask import request
import smtplib
import ssl
import os


my_password = os.getenv("MY_PASSWORD")
my_email = os.getenv("MY_EMAIL")


app = Flask(__name__)
@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def send_data():
    if request.method == "POST":
        send_email(request.form)
    return render_template("index.html")


def send_email(data):
    name = data["name"]
    email = data["email"]
    msg = data["message"]

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host='smtp.gmail.com',port=465 , context=context)as smtp :
        smtp.login(user=my_email ,password=my_password)
        smtp.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject:My WebSite\n\nNew Contact\nName:\t{name}\nEmail:\t{email}\nMessage:\n{msg}")

if __name__ == "__main__":
    app.run(debug=True)