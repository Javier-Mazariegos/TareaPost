from flask import Flask, url_for, request,redirect
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)
with open('data.json') as json_file:
    my_json = json.load(json_file)

@app.route('/')
def index():
    template = env.get_template('index.html')
    image_file = url_for('static',  filename ='libros.jpg')
    return template.render(my_data=my_json['data'], headers=my_json['headers'], image_file= image_file)


@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method == 'POST':
        _id = request.form['id']
        _libro = request.form['libro']
        _genero = request.form['genero']
        _paginas = request.form['paginas']
        _autor = request.form['autor']
        my_json['data'].append({"id":_id, "libro":_libro, "genero":_genero, "paginas":_paginas, "autor":_autor})
        return redirect(url_for('index'))
    template = env.get_template('form.html')
    return template.render()

if __name__ == "__main__":
    app.run(host="localhost",port=5000, debug=True)