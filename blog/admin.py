from django.db import models
from django.contrib import admin
from mdeditor.widgets import MDEditorWidget

from .models import Post,Tag,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_display = ['title', 'createTime', 'modifiedTime', 'category', 'author']


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
