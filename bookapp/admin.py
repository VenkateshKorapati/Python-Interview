from django.contrib import admin
from bookapp.models import BookShelf

class BookShelfAdmin(admin.ModelAdmin):
    list_display=['name','author','ISBN_number','publication','genre']

admin.site.register(BookShelf, BookShelfAdmin)
