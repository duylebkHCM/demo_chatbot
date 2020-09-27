from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, abort, flash, current_app
from werkzeug.utils import secure_filename
from requests.sessions import session
from http.client import responses
from subprocess import Popen, PIPE
import http.client
import async_timeout
import requests
import aiohttp
import asyncio
import os
import re

loop = asyncio.get_event_loop() 

app = Flask(__name__)

app.secret_key = "le anh duy"
path = os.getcwd()
UPLOAD_PATH_1 = os.path.join(path, 'data')
UPLOAD_PATH_3 = os.path.join(path, 'config')
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*5 #5MB
app.config['UPLOAD_EXTENSIONS'] = set(['.md', '.yml'])
app.config['UPLOAD_PATH_1'] = UPLOAD_PATH_1
app.config['UPLOAD_PATH_2'] = path
app.config['UPLOAD_PATH_3'] = UPLOAD_PATH_3

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/train", methods =["POST"])
def train():
  print('DEBUG training...')
  # flash('Training...')
  # subprocess.call(['python', 'train_model_commandline.py'])
  process = Popen(['python', 'train_model_commandline.py'])
  final_output = []
  final_error = []
  ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
  process_status = process.wait()

  # while True:
  #   output = process.stdout.readline()
  #   error = process.stderr.readline()
  #   new_out = ansi_escape.sub('', output.decode('utf8', errors='strict'))
  #   print(new_out)
  #   final_output.append(new_out)
  #   new_err = ansi_escape.sub('', error.decode('utf8', errors='strict'))
  #   final_error.append(new_err)
  #   print(new_err)
  #   return_code = process.poll()

  #   if return_code is not None:
  #     break 

  # flash("Output: {}".format(",".join([i for i in final_output if len(i) > 0])))
  # flash("Error{}".format(",".join([i for i in final_error if len(i) > 0])))
  return redirect(url_for('index'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':

        # if 'files[]' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)

        # files = request.files.getlist('file_input')

        # for file in files:
        #     if file and allowed_file(file.filename):
        #         filename = secure_filename(file.filename)
        #         print('DEBUG filename', filename)
        #         if filename == 'domain.yml':
        #           file.save(os.path.join(app.config['UPLOAD_PATH_2'], filename))
        #         elif filename in ['stories.md', 'nlu.md']:
        #           file.save(os.path.join(app.config['UPLOAD_PATH_1'], filename))

      if request.method == "POST":

        file = request.files["file"]

        print("File uploaded")
        print(file)
        filename = secure_filename(file.filename)
        res = make_response(jsonify({"message": "File uploaded"}), 200)
        if filename == 'domain.yml':
          file.save(os.path.join(app.config['UPLOAD_PATH_2'], filename))
        elif filename in ['stories.md', 'nlu.md', 'responses.md']:
          file.save(os.path.join(app.config['UPLOAD_PATH_1'], filename))
        elif filename == 'config.yml':
          file.save(os.path.join(app.config['UPLOAD_PATH_3'], filename))
        return res

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)