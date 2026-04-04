from flask import Flask, request, render_template
import subprocess
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')

    sp = subprocess.Popen('ping -c 1 ' + ip, shell=True, stdout=subprocess.PIPE)
    subprocess_return = sp.stdout.read()

    return subprocess_return.decode('utf-8')

@app.route('/pinger', methods=['GET'])
def pingme():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
