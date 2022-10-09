from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Contact
# Create your views here.
def index(request):
    data = Contact.objects.all()
    # data = Contact.objects.all().values()
    print("data is..",data)
    context = {"data":data}
    return render(request, "index.html", context)
#  return HttpResponse('Hello, World!')


def contact(request):
    params = {"name":"Kishore Kumar"}
    return render(request, "contact.html", params)

    # return  HttpResponse('welcome to  page') 

@csrf_exempt
def addToDo(request):
     print(request.POST)
     if request.method == 'POST':
        title = request.POST.get("title")
        print("description",title)
        desc = request.POST.get("desc")
        print(desc)
        obj = Contact.objects.create(title =title, desc = desc)
        obj.save()
        return render(request, "addToDo.html")
     return render(request, "addToDo.html")
    