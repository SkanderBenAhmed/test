from unicodedata import category
from django.contrib import admin
from .models import Book,Author

#admin.site.register(Author)
#admin.site.register(Book)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("title","price","author","category")
    list_editable=("title",)
    list_display_links=("price", )
    search_fields=("title", )
    list_filter=("category",)
    list_per_page =10