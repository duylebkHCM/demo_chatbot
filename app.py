from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, abort, flash
from train_model_commandline import train_model
from werkzeug.utils import secure_filename
from run_server import run_server
import nest_asyncio
from subprocess import Popen
import asyncio
import http.client
import os

# nest_asyncio.apply()
# from run_nlu_server import 

# loop = asyncio.get_event_loop() 

app = Flask(__name__)

app.secret_key = "secret key"
path = os.getcwd()
UPLOAD_PATH_1 = os.path.join(path, 'data')
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*5 #5MB
app.config['UPLOAD_EXTENSIONS'] = set(['.md', '.yml'])
app.config['UPLOAD_PATH_1'] = UPLOAD_PATH_1
app.config['UPLOAD_PATH_2'] = path

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/train", methods =["POST"])
def train():
  # loop.run_until_complete(train_data())
  print('DEBUG training...')
  process = Popen(['python', 'train_model_commandline.py'])
  while process.poll() is None:
    continue
  flash('Complete training')
  return redirect(url_for('index'))

  # returned_value = os.system("gnome-terminal -x python train_nlu_commandline.py")
  # print('DEBUG start running nlu server ...')
  # # run_nlu()
  # if returned_value == 0:
  #   flash('Complete training')
  #   return redirect(url_for('index'))

@app.route("/run", methods =["POST"])
def run():
  process = Popen(['python', 'run_server.py'])
  flash('Start running nlu server')
  return redirect(url_for('index'))

@app.route("/stop", methods =["POST"])
def stop():
  # conn = http.client.HTTPConnection("localhost",5005)
  # conn.close()
  Popen(['python', 'run_server.py']).terminate()
  import psutil
  from signal import SIGKILL

  for proc in psutil.net_connections(kind = 'inet'):
    if proc.laddr[1] == 5005:
      p = psutil.Process(proc.pid)
      p.terminate()  
  flash('Stop running nlu server')
  return redirect(url_for('index'))

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

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
        elif filename in ['stories.md', 'nlu.md']:
          file.save(os.path.join(app.config['UPLOAD_PATH_1'], filename))

        return res

        # flash('File(s) successfully uploaded')
        # return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)