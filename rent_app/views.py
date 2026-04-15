from urllib import request
from django.shortcuts import render,HttpResponse
from.models import Contact,FeedBack
from django.contrib import messages

def all_feedback(request):
    ##select * from Feedback
  feedback_list=FeedBack.objects.all()
  feedback_dict={
      "feedback_key":feedback_list
  }
  return render(request,"rent_app/html/all_feedback.html",feedback_dict)
# Create your views here.
def home(request):
    # return HttpResponse("<h1>This is Home Page</h1>")
    return render(request,'rent_app/html/index.html')
def about_us(request):
    return render (request,'rent_app/html/about_us.html') 
def contact_us(request):
    if request.method == "GET":
        return render(request, 'rent_app/html/contact_us.html')
    if request.method == "POST":
        user_Email = request.POST["Email"]
        user_Name = request.POST["Name"]
        user_Phone = request.POST["Phone"]
        user_question = request.POST["question"]
        contact_obj = Contact(email=user_Email,name=user_Name,question=user_question,phone=user_Phone)
        contact_obj.save()
        messages.success(request,"🙏we will contact you as soon as possible.🙏")
        return render(request, 'rent_app/html/contact_us.html')
