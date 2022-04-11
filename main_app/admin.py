from django.contrib import admin
from .models import Channel, UserProfile, Thread, Photo


# Register your models here.
admin.site.register(Channel)
admin.site.register(UserProfile)
admin.site.register(Thread)
admin.site.register(Photo)