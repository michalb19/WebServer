from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_status/<number>')
def upload_status(number):
    return 'File %s was uploaded' % (number)

@app.route('/handle_upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'uploaded_file' in request.files:
            uploaded_file = request.files['uploaded_file']
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join('C:/Temp/Files', uploaded_file.filename))
            return redirect(url_for('upload_status', number=123456))
    else:
        return render_template('upload_form.html')

@app.route('/handle_download')
def download_file():
    return 'Downloading...'


if __name__ == '__main__':
    app.run()