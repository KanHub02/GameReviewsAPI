from django.contrib import admin
from .models import Game, Rating, Publisher, Tag


admin.site.register(Game)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Publisher)
# Register your models here.
