from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
import json
import datetime

def index(request):
    p1 = Post.objects.create(title="Fred Flintstone", publish_date=datetime.date.today(),
              content="Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.",
              author="David Cohen")
    p2 = Post.objects.create(title="Weblog system", publish_date=datetime.date.today(),
              content="What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.",
              author="Kfir Wilfand")
    p3 = Post.objects.create(title="Possible in Django", publish_date=datetime.date.today(),
              content="This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.",
              author="David Hero")
    p4 = Post.objects.create(title="Allows Referencing", publish_date=datetime.date.today(),
              content="The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.",
              author="Bon Jovi")

    return HttpResponse(Post.objects.all()
)
