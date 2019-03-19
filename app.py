from flask import Flask, request, Response, json, render_template
import fruit_generator
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/fruits', methods=['GET', 'POST'])
def get_all_fruits():
    if request.method == 'GET':
        request_size = request.args.get('size')
        fruits = fruit_generator.create_list(request_size)

        return json.dumps(fruits)
    else:
        return Response('It is not a GET method :(', status=405)


@app.route('/api/v1/fruits/<id>', methods=['GET', 'POST'])
def fruit_by_id(id):
    if request.method == 'GET':
        request_size = request.args.get('size')
        fruit = fruit_generator.create(id, request_size)

        return json.dumps(fruit)

    else:
        return Response('It is not a GET method :(', status=405)


@app.route('/api/v1/users', methods=['GET', 'POST'])
def login():
    if 'name' in request.form and 'surname' in request.form:
        return render_template('login.html', name=request.form['name'], surname=request.form['surname'])
    else:
        return render_template('login.html', name='Adele', surname='Adele')


@app.route('/api/v1/logged.html', methods=['GET', 'POST'])
def logged():
    if 'name' in request.form and 'surname' in request.form:
        return render_template('logged.html', name=request.form['name'], surname=request.form['surname'])
    else:
        return render_template('logged.html', name='Adele', surname='Adele')



if __name__ == '__main__':
    app.run()
