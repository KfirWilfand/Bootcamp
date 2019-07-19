from bottle import route, run, static_file, error


@error(404)
def page_not_found(error):
    return static_file('404.html', root='')

if __name__ == "__main__":
    run(host='localhost', port=7001)