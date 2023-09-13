from django.contrib import admin
from .models import Products, Category_goods, Order, Products_Review, Profile

class ProductsReviewAdmin(admin.ModelAdmin):
    list_display = (('products', 'date_created', 'reviewer', 'content'))

admin.site.site_header = "E-parduotuve"
admin.site.site_title = "Apsipirkimas"
admin.site.index_title = "Valdymas"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,reqest,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'default Category'
    list_display = ('title','price', 'discount_price','Category_goods', 'description', 'image')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    # fields=('title',)
    list_editable = ('price',)

admin.site.register(Products,  ProductAdmin)
admin.site.register(Category_goods,)
admin.site.register(Order)
admin.site.register(Products_Review, ProductsReviewAdmin)
admin.site.register(Profile)