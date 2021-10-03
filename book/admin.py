from django.contrib import admin
from book.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display =  ('title')
    search_fields = ('title')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Book)