from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, abort, flash
from train_model_commandline import train_model
from werkzeug.utils import secure_filename
from run_server import run_server
from subprocess import Popen
import http.client
import os

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
  print('DEBUG training...')
  process = Popen(['python', 'train_model_commandline.py'])
  process2 = Popen(['python','gen.py'])
  while process.poll() is None:
    continue
  flash('Complete training')
  return redirect(url_for('index'))

@app.route("/run", methods =["POST"])
def run():
  process = Popen(['python', 'run_server.py'])
  process2 = Popen(['rasa','run','actions'])
  flash('Start running nlu server')
  return redirect(url_for('index'))

@app.route("/stop", methods =["POST"])
def stop():
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
  if request.method == "POST":

    file = request.files["file"]

    print("File uploaded")
    print(file)
    filename = secure_filename(file.filename)
    res = make_response(jsonify({"message": "File uploaded"}), 200)
    if filename == 'domain.yml':
      print(app.config['UPLOAD_PATH_2'])
      file.save(os.path.join(app.config['UPLOAD_PATH_2'], filename))
    elif filename in ['stories.md', 'nlu.md']:
      file.save(os.path.join(app.config['UPLOAD_PATH_1'], filename))

    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)