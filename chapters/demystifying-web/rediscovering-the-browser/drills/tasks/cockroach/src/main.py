from flask import Flask, request
app = Flask(__name__)

@app.route('/cockroach', methods=['DELETE'])
def delete_this_bastard():
    return "SSS{you_smashed_it}"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
