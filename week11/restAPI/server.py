from bottle import route, run, get, request, post
from pymysql import connect, cursors
import json

connection = connect(host='localhost', user='root', password='root',
                     db='imdb', charset='utf8', cursorclass=cursors.DictCursor)


@get('/student')
def getStudentById():
    id = request.query.id

    if id:
        query = "SELECT * FROM bootcamp.students WHERE `first_name`= {} ".format(id)
        isStudentExist = executeQuery(query)

        if not isStudentExist:
            return printMsg("Error", 'Student doest exist!', {'query': query})

        return executeQuery("SELECT * FROM bootcamp.students WHERE `student_id`= " + id)
    else:
        return executeQuery("SELECT * FROM bootcamp.students")


@post('/student/add')
def getStudentById():
    forms = request.forms

    firstName = forms["firstName"]
    lastName = forms["lastName"]
    cohort = forms["cohort"]

    if firstName and lastName and cohort:

        return executeQuery(
            "INSERT INTO bootcamp.students (`first_name`,`last_name`,`cohort`) VALUES ('{}','{}',{})".format(
                firstName, lastName, cohort))

    else:
        return printMsg("Error", 'missing parameters')


@post('/student/update')
def getUpdateStudent():
    forms = request.forms

    id = forms["id"]
    firstName = forms["firstName"]
    lastName = forms["firstName"]
    cohort = forms["cohort"]

    if id and firstName and lastName and cohort:
        if not isStudentExist(id):
            return printMsg("Error", 'Student doesnt exist!')

        return executeQuery(
            "UPDATE bootcamp.students SET `first_name` = '{}', `last_name` = '{}', `cohort` = {} WHERE `student_id` = {};".format(
                firstName, lastName, cohort, id))
    else:
        return printMsg("Error", 'missing parameters')


@post('/student/update')
def getUpdateStudent():
    forms = request.forms

    id = forms["id"]
    firstName = forms["firstName"]
    lastName = forms["firstName"]
    cohort = forms["cohort"]

    if id and firstName and lastName and cohort:
        if not isStudentExist(id):
            return printMsg("Error", 'Student doesnt exist!')

        return executeQuery(
            "UPDATE bootcamp.students SET `first_name` = '{}', `last_name` = '{}', `cohort` = {} WHERE `student_id` = {};".format(
                firstName, lastName, cohort, id))
    else:
        return printMsg("Error", 'missing parameters')


@post('/student/delete')
def getUpdateStudent():
    forms = request.forms

    id = forms["id"]

    if id:
        if not isStudentExist(id):
            return printMsg("Error", 'Student doesnt exist!')

        return executeQuery(
            "DELETE FROM bootcamp.students WHERE `student_id` = '{}'".format(id))
    else:
        return printMsg("Error", 'missing parameters')


def isStudentExist(studentId):
    return executeQuery("SELECT * FROM bootcamp.students WHERE `student_id` = {}".format(studentId))


def executeQuery(sqlQuery):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            if cursor.rowcount == 0:
                return 0
            else:
                result = cursor.fetchall()
                return json.dumps(result)
    except:
        return printMsg("Error", 'somthing is worng with the DB', {'query': sqlQuery})


def printMsg(type, msg, element={"element": "no element to display"}):
    return json.dumps([{type: msg}, element])


if __name__ == "__main__":
    run(host='localhost', port=7000, debug=True)
