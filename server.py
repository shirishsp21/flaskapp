from flask import Flask, request, render_template, url_for, redirect
import csv
import sys

app = Flask(__name__)

# To run: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# set FLASK_APP=server.py
# set FLASK_ENV=development   # this enables debug mode. web reloads with file changes in debug mode.
#

# HTML files are stored in 'template' folder.
# Static files (js, css) are stored in 'static' folder with HTML files referencing them from 'static/..' folder
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files

# favicon: https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/?highlight=favicon

# routing: variable rules: https://flask.palletsprojects.com/en/1.1.x/quickstart/?highlight=variable%20rules#variable-rules


# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     # url_for is a method in flask which we can print here using:
#     print(f'Favicon URL is:', url_for('static', filename='favicon.ico'))
#     return render_template('index.html', name=username, post_id=post_id)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{email},{subject},{message}')


# when using CSV reader or writer we use newline='' to read/write the newline.
# https://docs.python.org/3/library/csv.html#csv.reader
# https://docs.python.org/3/library/csv.html#csv.writer
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer = csv.writer(database, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file = writer.writerow([email, subject, message])


@app.route('/')
def home():
    # url_for is a method in flask which we can print here using:
    # print(f'Favicon URL is:', url_for('static', filename='favicon.ico'))
    return render_template('index.html')


@app.route('/<string:page_name>.html')
def index(page_name):
    return render_template(f'{page_name}.html')

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thank_you.html')
        except TypeError as terr:
            print(terr)
            return 'did not save to database!'
        except:  # catch all exceptions.
            e = sys.exc_info()[0]
            print(e)
            return 'did not save to database!'
    else:
        return 'something went wrong in form submit'

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'
