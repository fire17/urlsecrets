from flask import Flask

app = Flask(__name__)

#@app.route('/')
#def hello():
#    return 'yooooooo'

@app.route('/')
def root():
    return app_response_code()

@app.route('/redirect')
def redirect():
    return '''  <script type="text/javascript">
                var token = window.location.href.split("#")[1];
                window.location =  token;
            </script> '''

@app.route('/<response>', methods=['GET'])
def app_response_code(response={}):
    return '''  <script type="text/javascript">
                var token = window.location.href.split("#")[1]; 
                window.location = "/app_response_token/" + token;
            </script> '''

@app.route('/app_response_token/<token>/', methods=['GET'])
def app_response_token(token):
    return token


#def hello():
#    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
