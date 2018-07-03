from flask import *

app = Flask(__name__)

app.config['SECTRET_KEY'] = 'thisisandela'

@app.route('/', methods=['POST', 'GET'])
def create():
    data = request.get_json()
    Name = data['Name']
    Email = data['Name']
    Username = data['Username']
    Password = data['Password']
    details.update({"Name": Name, "Email": Email, "Username" : Username, "Password": Password})

    return jsonify({"Message": "Registration successfull"})

if __name__ == '__main__':
    app.run(debug=True, port=8312)
