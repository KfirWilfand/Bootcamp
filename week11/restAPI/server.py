from bottle import route, run, get, request, post,put
from pymysql import connect, cursors
import json

connection = connect(host='localhost', user='root', password='root',
                     db='bootcamp', charset='utf8', cursorclass=cursors.DictCursor)


@get('/student')
def get_student_by_id():
    id = request.query.id

    if id:
        query = "SELECT * FROM students WHERE `first_name`= {} ".format(id)
        is_student_exist = execute_query(query)

        if not is_student_exist:
            return generate_json_msg("Error", 'Student doest exist!', {'query': query})

        return execute_query("SELECT * FROM students WHERE `student_id`= " + id)
    else:
        return execute_query("SELECT * FROM students")


@post('/student')
def get_student_by_id():
    forms = request.forms

    first_name = forms["first_name"]
    last_name = forms["last_name"]
    cohort = forms["cohort"]

    if first_name and last_name and cohort:

        return execute_query(
            "INSERT INTO bootcamp.students (`first_name`,`last_name`,`cohort`) VALUES ('{}','{}',{})".format(
                first_name, last_name, cohort))

    else:
        return generate_json_msg("Error", 'missing parameters')


@put('/student/<id>')
def get_update_student(id):
    forms = request.forms

    first_name = forms["first_name"]
    last_name = forms["last_name"]
    cohort = forms["cohort"]

    if id and first_name and last_name and cohort:
        if not is_student_exist(id):
            return generate_json_msg("Error", 'Student doesnt exist!')

        return execute_query(
            "UPDATE bootcamp.students SET `first_name` = '{}', `last_name` = '{}', `cohort` = {} WHERE `student_id` = {};".format(
                first_name, last_name, cohort, id))
    else:
        return generate_json_msg("Error", 'missing parameters')

@post('/student/delete')
def get_update_student():
    forms = request.forms

    id = forms["id"]

    if id:
        if not is_student_exist(id):
            return generate_json_msg("Error", 'Student doesnt exist!')

        return execute_query(
            "DELETE FROM bootcamp.students WHERE `student_id` = '{}'".format(id))
    else:
        return generate_json_msg("Error", 'missing parameters')


def is_student_exist(student_id):
    return execute_query("SELECT * FROM bootcamp.students WHERE `student_id` = {}".format(student_id))


def execute_query(sql_query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            if cursor.rowcount == 0:
                return 0
            else:
                result = cursor.fetchall()
                return json.dumps(result)
    except:
        return generate_json_msg("Error", 'somthing is worng with the DB', {'query': sql_query})


def generate_json_msg(type, msg, element={"element": "no element to display"}):
    return json.dumps([{type: msg}, element])


if __name__ == "__main__":
    run(host='localhost', port=7000, debug=True)
