from flask import *
import ezgmail

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if (request.method == 'POST'):

        subject = "website email"
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        body = "Name: {} \nEmail: {} \nMessage: {}".format(
            name, email, message)

        if name != "" and email != "" and message != "":
            ezgmail.send('shyamraj0805@gmail.com', subject, body)

    return render_template('index.html')
