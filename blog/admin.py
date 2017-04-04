from django.contrib import admin
from .models import Post # the inherited one can be a inheriter like this way!

# Register your models here.
admin.site.register(Post)