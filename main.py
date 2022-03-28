from flask import Flask, render_template, url_for, request
from flask import Flask, render_template, request, jsonify, make_response, session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


# localhost:5000/
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/counter")
def counter_page():
    print(session)
    if not session.get('counter'):
        session['counter'] = 1
        return '1'
    else:
        counter = session['counter']
        counter += 1
        session['counter'] = counter
        return str(counter)


@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    # return f'GOT it <br /> {str(request.form)}'
    return f'Your name is {request.form["txt_name"]}'


app.run()
