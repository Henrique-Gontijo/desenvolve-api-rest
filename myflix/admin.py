from django.contrib import admin
from myflix.models import User, Stream

class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'cell_phone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(User, Users)

class Streams(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
    list_display_links = ('id', 'code')
    search_fields = ('code', 'description')

admin.site.register(Stream, Streams)