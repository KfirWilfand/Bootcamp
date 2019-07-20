import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils

# Static Routes


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=utils.getData())


@get("/ajax/show/<showId>")
def show(showId):
    sectionTemplate = "./templates/show.tpl"
    return template(sectionTemplate, result=utils.getDataById(showId))


@get("/ajax/show/<showId>/episode/<episodeId>")
def episode(showId, episodeId):
    sectionTemplate = "./templates/episode.tpl"
    return template(sectionTemplate, result=utils.getEpisodeById(showId, episodeId))


@get("/show/<showId>")
def show(showId):
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=utils.getDataById(showId))


@get("/show/<showId>/episode/<episodeId>")
def episode(showId, episodeId):
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=utils.getEpisodeById(showId, episodeId))


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData="{}")


@post('/search')
def search():
    sectionTemplate = "./templates/search_result.tpl"
    query = request.forms.get('q')
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData="{}", query=query, results=utils.search(query))


run(host='localhost', port=os.environ.get('PORT', 5000))
