from flask import Flask, jsonify, request, session, make_response, render_template, url_for
from functools import wraps
import jwt
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'JustDemonstrating'

token = ''

def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Missing Token'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return func(*args, **kwargs)
    return wrapped

@app.route('/public')
def public():
    return '<h1>Anyone can view this</h1>'

@app.route('/auth')
@check_for_token
def authorised():
    return 'This is only viewable with a token'

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth.username == 'a' and auth.password == 'b':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return make_response('Unable to verify', 403, {'WWW.Authenticate': 'Basic'})


if __name__ == '__main__':
    app.run(debug=True)
