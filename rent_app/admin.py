from django.contrib import admin

# Register your models here.
from .models import FeedBack,Contact,User,Owner
admin.site.register(FeedBack)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Owner)