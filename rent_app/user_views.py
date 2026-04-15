from django.shortcuts import render,HttpResponse,redirect
from.models import FeedBack
from.models import User,Product
from django.contrib import messages

def user_logout(request):
   request.session.flush()##it will kill/destroy the session
   messages.success(request,"Successfully Logged Out, THANK YOU🙏")
   return redirect("user_login")

def user_login(request):
    if request.method=="GET":
       return render(request,'rent_app/user/user_login.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        userList=User.objects.filter(email=user_email,password=user_password) 

        if len(userList)>0:
            #user_object=userList[0]
            request.session["user_key"]=user_email
            #request.session["user_role"]="user"
            return redirect("user_home")
        else:
           messages.error(request,"😈Invalid Credential😈")
           return redirect("user_login")

def user_reg(request):
   


   #return render(request, 'rent_app/user/user_registration.html')

   if request.method=="GET": ##HTTP protocol method
      return render(request, 'rent_app/user/user_registration.html')
   if request.method=="POST":
      user_name=request.POST["name"] ##it will read data from the textbox
      user_email=request.POST["email"]
      user_password=request.POST["password"]
      user_phone=request.POST["phone"]
      user_pic=request.FILES.get("profile_pic")
      user_reg_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
      user_reg_obj.save()##it will store data into database table
      messages.success(request,"😊Thanku For Your Time😊")
      # return render(request, 'rent_app/user/user_feedback.html')
      return redirect("user_login")##logical name of your URl enpoint


def user_feedback(request):
    if request.method=="GET": ##HTTP protocol method
     user_email=request.session["user_key"]##getting email from session
     user_obj=User.objects.get(email=user_email)
     user_dict={"user_detail":user_obj}

     return render(request, 'rent_app/user/user_feedback.html',user_dict)
    

    if request.method=="POST":
      user_name=request.POST["name"] ##it will read data from the textbox
      user_email=request.POST["email"]
      user_rating=request.POST["rating"]
      user_remark=request.POST["remark"]
      profile_pic=request.POST["pic_path"]
      feedback_obj=FeedBack(email=user_email,name=user_name,rating=user_rating,remark=user_remark,user_pic=profile_pic)
      feedback_obj.save()##it will store data into database table
      messages.success(request,"😊Thanku For Your Time😊")
      # return render(request, 'rent_app/user/user_feedback.html')
      return redirect("user_feedback")##logical name of your URl enpoint

def user_home(request):
    
    if request.method=="GET":
      #GET method help to show data
     #fetch/get the value from session
      user_email=request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      #select *from User where email=user_email
      #sending object from view to template
      #create a dictionary and bind object with a key 
      # and send the dictionary
      user_dict={"user_info":user_obj}


      return render(request, 'rent_app/user/user_home.html',user_dict)
def view_product(request):
   if request.method=="GET":
      product=Product.objects.all()
      product_dict={"product_key":product}
      return render(request, 'rent_app/user/view_product.html',product_dict)
   if request.method=="POST":
      category=request.POST["category"]
      product=Product.objects.filter(product_category=category)
      product_dict={"product_key":product}
      return render(request, 'rent_app/user/view_product.html',product_dict)
