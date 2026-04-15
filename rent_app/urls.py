from django.urls import path,include
from .import views,user_views,owner_views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact_us,name="contact_us"),
    path("user_login/",user_views.user_login,name="user_login"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    
    path("user_reg/",user_views.user_reg,name="user_registration"),
    path("user_feedback/",user_views.user_feedback,name="user_feedback"),
    path("user_home/",user_views.user_home,name="user_home"),
    path("owner_login/",owner_views.owner_login,name="owner_login"),
    path("owner_home/",owner_views.owner_home,name="owner_home"),
    path("owner_reg/",owner_views.owner_reg,name="owner_reg"),
    path("all_feedback/",views.all_feedback,name="all_feedback"),
    path("add_product/",owner_views.add_product,name="add_product"),
    path("view_product/",user_views.view_product,name="view_product"),
    path("Inventory/",owner_views.inventory,name="Inventory"),
    path("manage_inventory/<str:id>",owner_views.manage_inventory,name="manage_inventory"),
    path("manage_inventory_post/",owner_views.manage_inventory_post,name="manage_inventory_post"),
    

]