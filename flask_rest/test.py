from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['SECTRET_KEY'] = 'thisisandela'

@app.route('/', methods= ['GET'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        name = some_json['name']
        return jsonify({"you sent": some_json}), 201
    else:
        return jsonify({"Homepage": "Hello world"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

if __name__ == '__main__':
    app.run(debug=True, port=5999)