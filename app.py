from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Welcome to Flask Authentication App by J Morkly'

def validate_credentials(username, password):
    if username == 'admin' and password == 'password':
        return True
    return False

@app.route('/' , methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        if username == '' or password == '':
            error_msg = "Invalid username or password"
            return render_template('index.html', error=error_msg)
        if validate_credentials(username, password):
            return home()
        error_msg = "Invalid username or password"
        return render_template('index.html', error=error_msg)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()