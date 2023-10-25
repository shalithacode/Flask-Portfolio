from flask import Flask, render_template,request,redirect,url_for
import csv, os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not email or not subject or not message:
            return redirect(url_for('contact'))  

        file_exists = os.path.isfile("database.csv")

        with open('database.csv', mode='a',newline='') as db:
            csv_writer = csv.writer(db, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if not file_exists:
                csv_writer.writerow(["email", "subject", "message"])
            csv_writer.writerow([email, subject, message])



    return redirect("/thankyou.html")