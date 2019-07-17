from bottle import route, run
from jinja2 import Template
numOfAccessed = 0

@route('/')
def index():
    global numOfAccessed 
    numOfAccessed = numOfAccessed + 1
    template = Template(
        '<h3>This server has benn accessed {{ numOfAccessed }} times</h3>')
    return template.render(numOfAccessed=numOfAccessed)


if __name__ == "__main__":
    run(host='localhost', port=7000, debug=True)
