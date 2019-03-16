from flask import Flask, request, Response, json
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


if __name__ == '__main__':
    app.run()
