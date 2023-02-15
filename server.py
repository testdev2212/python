from asyncore import write
from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)
# print(__name__)
@app.route("/<string:page_name>")
def page(page_name=None):
    return render_template(page_name)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'note save to db'
    else:
        return 'something when wrong'

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])