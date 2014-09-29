from django.contrib import admin

# Register your models here.
from fix_it.models import Post, Annotate, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Annotate)
class AnnotateAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
