from flask import Flask, render_template, request, url_for, redirect, send_file

import FileServer
import config

app = Flask(__name__)
file_server = FileServer.FileServer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_status/<code>')
def upload_status(code):
    if code == '':
        return 'Failed uploading file'
    file_status = file_server.get_file_status(code)
    return 'File no. %s was uploaded successfully and downloaded %d times (refresh for updates)' % (code, file_status)

@app.route('/handle_upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'uploaded_file' in request.files:
            uploaded_file = request.files['uploaded_file']
            code = file_server.save_upload_file(uploaded_file)
            return redirect(url_for('upload_status', code=code))

    return render_template('upload_form.html')

@app.route('/handle_download')
def download_file():
    if 'code' in request.args:
        download_file = file_server.get_download_filepath(request.args['code'])
        if download_file  is not None:
            return send_file(download_file[config.SERVER_PATH_INDEX], as_attachment=True, 
                attachment_filename=download_file[config.ORIGINAL_FILENAME_INDEX])
        return 'Failed finding requested file to download'
    return render_template('download_form.html')


if __name__ == '__main__':
    app.run()
