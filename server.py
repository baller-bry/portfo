from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
@app.route("/<html_file>")
def route(html_file="index.html"):
    return render_template(html_file)

def write_to_csv(data):
    with open("database.csv", 'a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)

            return redirect("/thankyou.html")
        except:
            return "Did not save to database."
    else:
        return "Something went wrong. Try again."