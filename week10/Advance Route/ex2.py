import bottle
import random
from bottle import route, run

@route('/')
def index():
 return random.choice(['red', 'green', 'orange', 'black', 'yellow', 'blue'])

def main():
 run(host='localhost', port=7000)

if __name__ == '__main__':
 main()
