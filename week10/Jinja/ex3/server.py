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

    instructions = ""

    if user["firstName"][0].lower() == 'g':
        instructions = '<li>Send us email</li><li>Attach to the email...</li>'
    else :
        instructions = '<li>Fill in our winners...</li>'

    instructions += '<li>Wait for a reply</li>'

    template = Template(
        '<h1>Welcome {{user["firstName"]}} </h1>' +
        '<h3>We are very happy to greet you {{user["firstName"]}} {{user["lastName"]}}! <h3>'
        '<ul>{{instructions}}</ul>')

    return template.render(instructions=instructions,user=user)

if __name__ == "__main__":
    run(host='localhost', port=7001, debug=True)
