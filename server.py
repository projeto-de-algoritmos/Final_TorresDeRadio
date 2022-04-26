from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_bootstrap import Bootstrap
from algoritmos import color_test
from algoritmos import graph_visualization

import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "data.txt"))
            return redirect(url_for("home"))

    if request.method == 'GET':

        try:
            with open('static/files/data.txt', 'r') as file:
                data = file.read()
                lines = data.split('\n')

                for line in lines:
                    values = line.split(',')
                    print(f"valor 1: {int(values[0])} valor 2: {int(values[1])} ")

                g1 = [[] for i in range(6)]
                g1 = color_test.addEdge(g1, 0, 2)
                g1 = color_test.addEdge(g1, 1, 2)
                g1 = color_test.addEdge(g1, 1, 3)
                g1 = color_test.addEdge(g1, 5, 3)
                g1 = color_test.addEdge(g1, 3, 4)
                g1 = color_test.addEdge(g1, 1, 0)
                print("Coloring of graph 1 ")
                color_dict = color_test.greedyColoring(g1, 6)

                G = graph_visualization.GraphVisualization()
                G.addEdge(0, 2)
                G.addEdge(1, 2)
                G.addEdge(1, 3)
                G.addEdge(5, 3)
                G.addEdge(3, 4)
                G.addEdge(1, 0)
                G.visualize(color_dict)

                return render_template("index.html")

        except FileNotFoundError:
            print("This file does not exist")

        return render_template("index.html")


@app.route("/add_schedule", methods=['GET', 'POST'])
def add_schedule():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('view_schedule'))

    if request.method == 'GET':
        return render_template("wis_input.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)
