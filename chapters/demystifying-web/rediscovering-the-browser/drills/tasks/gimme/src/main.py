from flask import Flask, request
app = Flask(__name__)

@app.route('/gimme', methods=['POST'])
def post_method_with_content_type():
    body = request.data
    flag = "SSS{dont_forget_the_content_length}"

    if not body:
        return "Did you miss something ?"

    if len(body) == len(flag):
        return flag

    return "Not great, not terrible ! You should try 35 :)"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
