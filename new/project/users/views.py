# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# def users(request):
#     return HttpResponse("Hello world!")


from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('allUsers.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

  # template = loader.get_template('firstFile.html')
  # return HttpResponse(template.render())

def details(request, id):
  mymember = User.objects.get(id=id)
  template = loader.get_template('usersDetails.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('testTemplate.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

def testing2(request):
  mydata = User.objects.all()
  template = loader.get_template('dbData.html')
  context = {
    'myusers' : mydata
  }
  return HttpResponse(template.render(context, request))

def firstname(request):
  mydata = User.objects.values_list('firstname')
  template = loader.get_template('firstname.html')
  context = {
    'myusers' : mydata
  }
  return HttpResponse(template.render(context, request))

def lastname(request):
  mydata = User.objects.values_list('lastname')
  template = loader.get_template('lastname.html')
  context = {
    'myusers' : mydata
  }
  return HttpResponse(template.render(context, request))

def filter(request):
  mydata = User.objects.filter(firstname= 'Deepak').values()
  template = loader.get_template('filter.html')
  context = {
    'myusers' : mydata
  }
  return HttpResponse(template.render(context, request))

def css(request):
  template = loader.get_template('cssstatic.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))