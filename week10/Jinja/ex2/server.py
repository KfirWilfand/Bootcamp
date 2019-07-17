from bottle import route, run, request, post, get
from jinja2 import Template

@route('/')
def index():
    template = Template(
        '<form action="/add" method="POST">' +
        '<input name="firstName"></input>' +
        '<input name="lastName"></input>' +
        '<input type="submit" value="Signup">' +
        '</form>')
    return template.render()

@route('/add', method="POST")
def add_fruit():
    user = {
        "firstName": request.forms.get("firstName"),
        "lastName": request.forms.get("lastName")
    }

    template = Template(
        '<h1>Welcome {{user["firstName"]}} <h1>' +
        '<h3>We are very happy to greet you {{user["firstName"]}} {{user["lastName"]}}! <h1>')

    return template.render(user=user)

if __name__ == "__main__":
    run(host='localhost', port=7001, debug=True)
