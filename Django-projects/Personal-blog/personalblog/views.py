from django.shortcuts import render
from django.http import HttpResponse

projectlist = [
    {
        id : '1',
        'title' : 'Ecommerce website',
        'description' : 'Fully functional E-comm website'
    },
        {
        'id' : '2',
        'title' : 'Portfolio website',
        'description' : 'Fully functional Portfolio website'
    },
        {
        'id' : '3',
        'title' : 'Social Network',
        'description' : 'Still working on ocial Network'
    }
]


def homepage(request):
    projects = {'projects' : projectlist }
    return render(request, 'personalblog/home.html' , projects)

def product(request, pk):
    projectObj = None
    for project in projectlist:
        if project['id'] == pk:
            projectObj = project
    return render(request, 'personalblog/projects.html' , {'project' : projectObj})