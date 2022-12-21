from flask import Flask,request,render_template,redirect,flash,url_for,session
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from config import mail_username,mail_password 

app = Flask(__name__)
Bootstrap(app)

app.secret_key='secret123'
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route('/')
def home():

     return render_template("home.html")

@app.route('/project1')
def project1():

     return render_template("project_page.html")

@app.route('/project2')
def project2():

     return render_template("project_page1.html")

@app.route('/resume')
def resume():

     return render_template("resume.html")

@app.route('/resume_down')
def resume_down():

     return render_template("resume_down.html")


@app.route('/contact',methods=['GET','POST'])
def contact():
     if request.method == 'POST':
          name = request.form.get('name')
          sub = request.form.get('sub')
          email = request.form.get('email')
          phone = request.form.get('phone')
          message = request.form.get('message')
          msg = Message(
               subject = f"Mail from {name}", body=f"Name : {name}\n E-Mail : {email}\n Phone : {phone}\n\nSubject : {sub}\nMessage : {message}",sender=mail_username,recipients=['vignesh510510@gmail.com'])
          mail.send(msg)
          return render_template("contact.html", success=True)

     return render_template("contact.html")

@app.route('/hire', methods=['GET','POST'])
def hire():
      if request.method == 'POST':
          sub = request.form.get('sub')
          name = request.form.get('name')
          email = request.form.get('email')
          phone = request.form.get('phone')
          message = request.form.get('message')
          date = request.form.get('date')
          msg = Message(
               subject = f"Mail from {name}", body=f" Name : {name}\n E-Mail : {email}\n Phone : {phone}\n Date : {date}\n\n Subject : {sub}\n Message : {message}",sender=mail_username,recipients=['vignesh510510@gmail.com'])
          mail.send(msg)
          return render_template("hire-me.html", success=True)
      return render_template("hire-me.html")


if __name__ == '__main__':
    app.run(debug = True)