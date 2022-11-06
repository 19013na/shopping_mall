from django.contrib import admin
from .models import Product, Publisher, Category, Tag

admin.site.register(Product)

class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('publisher',)}

admin.site.register(Publisher, PublisherAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Tag, TagAdmin)


# Register your models here.
