import os
from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
from model import run_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file1 = request.files['file1']
    file2 = request.files['file2']
    if file1.filename == '':
        flash('No selected file!')
        return redirect(request.url)
    else:
        filename = secure_filename(file1.filename)
        content_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file1.save(content_path)
    
    if file2.filename == '':
        flash('No selected file!')
        return redirect(request.url)
    else:
        filename = secure_filename(file2.filename)
        style_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file2.save(style_path)
    
    image = run_model(content_path, style_path)

    return render_template('index.html', image=image)

