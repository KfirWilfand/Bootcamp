import bottle
from bottle import route, run
@route('/')
def index():
 return "Hello world"
def main():
 run(host='localhost', port=7000)
if __name__ == '__main__':
 main()
