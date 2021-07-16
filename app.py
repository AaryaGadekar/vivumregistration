from flask import Flask, render_template, url_for, redirect, request
import hashlib
from flask_sslify import SSLify
app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index():
    # return render_template('homepage.html', error_message='')
    if 'error_message' in request.args:
        return render_template('homepage.html', error_message=request.args['error_message'])
    else:
        return render_template('homepage.html', error_message='')


@app.route('/forms', methods=["GET", "POST"])
def forms():
    def loadHashes():
        hashes = set()
        with open('codes.txt', 'r') as file:
            for row in file:
                hashes.add(row.strip())
        return hashes

    if request.method == "GET":
        return redirect(url_for('index'))
    else:
        ans = str(request.form['code']).encode()
        if hashlib.sha256(ans).hexdigest() in loadHashes():
            return render_template('forms.html', school_name=request.form['code'])
        else:
            print(request.form['code'])
            print(str(hash(request.form['code'])))
            return redirect(url_for('index', error_message='Please enter a valid school code. If you do not have a school code, or would like your school to be sent one, please contact vivum20@tisb.ac.in.'))

if __name__ == '__main__':
    app.run(debug=True)
