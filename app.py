from flask import Flask, request, Response, json, render_template
import fruit_generator
import json

app = Flask(__name__)
fruits_cash = dict()


@app.route('/')
def hello_world():
    return 'Hello World!'


def request_validator(request):
    return request.form['id'] is not None and request.form['title'] is not None and \
           request.form['size'] in fruit_generator.SIZES


def check_authorization(request):
    pass


@app.route('/api/v1/fruits', methods=['GET', 'POST'])
def get_all_fruits():
    if request.method == 'GET':
        request_size = request.args.get('size')
        random_fruits = fruit_generator.create_list(request_size)
        fruits = list(fruits_cash.values()) + random_fruits
        return json.dumps(fruits)

    elif request.method == 'POST':
        if request_validator(request):

            if request.headers['Authorization'] == 'admin':
                fruit = {
                    'id': request.form['id'],
                    'title': request.form['title'],
                    'size': request.form['size']
                }
                fruits_cash[request.form['id']] = fruit
                return Response('OK', status=201)

            elif request.headers['Authorization'] is None or request.headers['Authorization'] is not 'admin':
                return Response('Please authorize', status=403)
        else:
            return Response(status=400)

    else:
        return Response('Bed method', status=405)


@app.route('/api/v1/fruits/<id>', methods=['GET', 'POST'])
def fruit_by_id(id):
    if request.method == 'GET':
        request_size = request.args.get('size')
        fruit = fruit_generator.create(id, request_size)

        return json.dumps(fruit)

    elif request.method == 'POST':
        if request.form[id] in list(fruits_cash.keys()):
            return fruits_cash[id]

        else:
            return fruit_generator.create(id, None)

    else:
        return Response('Bed method', status=405)


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
