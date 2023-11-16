from django.contrib import admin
from .models import Film, Cinema, FilmScreening

admin.site.register(Film)
admin.site.register(Cinema)
admin.site.register(FilmScreening)
