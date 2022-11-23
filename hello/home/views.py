from django.shortcuts import render,HttpResponse
from datetime import  datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #  return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is about page")

def contact(request):
    if request.method == "POST":
        desc = request.POST.get('desc')
        print(desc)
        name = request.POST.get('Name')
        print(name)
        email = request.POST.get('email')
        print(email)
        Phone_no = request.POST.get('phone')
        print(Phone_no)
        contact = Contact(name=name, email=email, phone=Phone_no, desc=desc, date = datetime.today())
        contact.save()

       
    return render(request, 'Contact.html')
    # return HttpResponse("this is contact page")



