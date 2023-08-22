from django.contrib import admin
from .models import Logo,Cart,karusel,karusel_possitive,Contact
# Register your models here.

admin.site.register(Logo)
admin.site.register(karusel)
admin.site.register(karusel_possitive)
admin.site.register(Contact)




from django.contrib import admin
from .models import Category, SubCategory, Product, Cart
# Register your models here.

@admin.register(Category, SubCategory, Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    

admin.site.register(Cart)