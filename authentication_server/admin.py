from django.contrib import admin

# Register your models here.
from authentication_server.models import User

admin.site.register(User)
