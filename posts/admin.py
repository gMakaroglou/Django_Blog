from django.contrib import admin
from .models import Author, Category, Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('testsummer',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)



