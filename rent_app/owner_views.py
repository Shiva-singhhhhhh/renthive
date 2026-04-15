from django.shortcuts import render,HttpResponse,redirect
from.models import OwnerLogin,Owner,Product,Inventory
from django.contrib import messages

product_id=0

def owner_home(request):
       if request.method=="GET":
      #GET method help to show data
     #fetch/get the value from session
        owner_email=request.session["owner_key"]
        owner_obj=Owner.objects.get(email=owner_email)
      #select *from User where email=user_email
      #sending object from view to template
      #create a dictionary and bind object with a key 
      # and send the dictionary
       owner_dict={"user_info":owner_obj}


       return render(request, 'rent_app/owner/owner_home.html',owner_dict)
     

def owner_login(request):
       if request.method=="GET": ##HTTP protocol method
          return render(request, 'rent_app/owner/owner_login.html')
              
    
       if request.method=="POST":
        owner_email=request.POST["email"]
        owner_password=request.POST["password"]
        
       userList=Owner.objects.filter(email=owner_email,password=owner_password) 

       if len(userList)>0:
            #user_object=userList[0]
            request.session["owner_key"]=owner_email
            #request.session["owner_role"]="owner"
            return redirect("owner_home")
       else:
           messages.error(request,"😈Invalid Credential😈")
           return redirect("owner_login")

       

       
def owner_reg(request):
     if request.method=="GET":
          return render(request,'rent_app/owner/owner_reg.html') 
     if request.method=="POST":
      owner_name=request.POST["name"] ##it will read data from the textbox
      owner_email=request.POST["email"]
      owner_password=request.POST["password"]
      owner_phone=request.POST["phone"]
      owner_city=request.POST["city"]
      owner_add=request.POST["address"]
      owner_pic=request.FILES.get("profile_pic")
      owner_reg_obj=Owner(name=owner_name,email=owner_email,password=owner_password,phone=owner_phone,city=owner_city,address=owner_add,profile_pic=owner_pic)
      owner_reg_obj.save()##it will store data into database table
      messages.success(request,"😊Thanku For Your Time😊")
      # return render(request, 'rent_app/user/user_feedback.html')
      return redirect("owner_login")##logical name of your URl enpoint
     

def add_product(request):
    if request.method=="GET":
          return render(request,'rent_app/owner/add_product.html') 
    
    if request.method=="POST":
      email=request.session["owner_key"]
      Product_name=request.POST["product_name"] ##it will read data from the textbox
      Product_category=request.POST["category"]
      Product_description=request.POST["description"]
      Product_price=request.POST["price"]
      Product_pic=request.FILES.get("product_pic")
      print("fhjkl;gfgvhjk",Product_category)
      owner_obj=Owner.objects.get(email=email)
      Product_obj=Product(owner =owner_obj, product_name=Product_name,product_category=Product_category,product_description=Product_description,product_price=Product_price,product_pic=Product_pic)
      Product_obj.save()
      return render(request,'rent_app/owner/add_product.html')
    
def inventory(request):
    if request.method=="GET":
     email=request.session["owner_key"]
     owner=Owner.objects.get(email=email)
     product=Product.objects.filter(owner=email)
     product_dict={"product_key":product}
     return render(request,'rent_app/owner/Inventory.html',product_dict)
def manage_inventory(request,id):
    global product_id
    product_id=id
    if request.method=="GET":  
          data=Inventory.objects.filter(product_id=id)
          if len(data)>0:
               data=data[0]
          product_dict={
               "product_key":data
          }   
          return render(request,'rent_app/owner/Inventory_management.html',product_dict)

def manage_inventory_post(request):
       if request.method=="POST":
        email = request.session["owner_key"]
        phone = request.POST["phone"]
        duration =request.POST["duration"]
        return_date=request.POST["return_date"]
        id_proof=request.FILES["id_proof"]
        inventory_obj = Inventory(user_phone=phone,owner_email =email ,product_id=product_id, duration=duration,returndate=return_date,id_proof=id_proof)
        inventory_obj.save()
        messages.success(request,"Inventory adddd.........")
        return redirect("owner_home")