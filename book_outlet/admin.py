from django.contrib import admin

from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)   # cannot be used in conjunction with prepopulated_fields
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
