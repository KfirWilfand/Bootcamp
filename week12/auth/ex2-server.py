from bottle import route, run, get, request, post
from pymysql import connect, cursors
from jinja2 import Template
import json
import hashlib
import uuid

connection = connect(host='localhost', user='root', password='root',
                     db='secure_users', charset='utf8', cursorclass=cursors.DictCursor)


@get('/login')
@post('/login')
def login():
    if request.method == "POST":
        return handle_login(request)
    else:
        return is_valid_user_session_id(request)


def handle_login(request):
    forms = request.forms

    user_name = forms['user_name']
    user_pass = forms['user_pass']
    next_url = forms['next_url']
    return verfiy_user(user_name, user_pass, next_url)


def is_valid_user_session_id(request):
    forms = request.forms
    user_name = forms['user_name']
    user_pass = forms['user_pass']
    session_id = forms['session_id']
    next_url = forms['next_url']

    hashed_password = hash_pass(user_pass)
    result = execute_query(
        "SELECT * FORM user WHERE user_name ='{}' AND user_password = '{}' AND session_id = '{}';".format(user_name,
                                                                                                          hashed_password,
                                                                                                          session_id))
    if result:
        return update_user_session_id(user_name, hashed_password, next_url)
    return False


def verfiy_user(user_name, user_pass, next_url):
    hashed_password = hash_pass(user_pass)
    result = execute_query(
        "SELECT * FORM user WHERE user_name ='{}' AND user_password = '{}';".format(user_name, hashed_password))
    if result:
        return update_user_session_id(user_name, hashed_password, next_url)
    return json.dumps({"STATUS": "Failed"})


def hash_pass(password):
    return hashlib.md5((password).encode('utf-8')).hexdigest()


def update_user_session_id(user_name, hashed_password, next_url):
    session_id = str(uuid.uuid4().hex)[:8]
    execute_query("UPDATE user SET session_id = '{}' WHERE user_name ='{}' AND user_password = '{}';".format(session_id,
                                                                                                             user_name,
                                                                                                             hashed_password))
    return json.dumps({"STATUS": "SUCCESS", 'SESSION_ID': session_id, 'NEXT_URL': next_url})


def execute_query(self, query):
    try:
        print({'DEBUG DB': {'query': query}})
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            self._connection.commit()
            return result
    except:
        json.dumps({"STATUS": "Failed"})
