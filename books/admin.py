from django.contrib import admin

from .models import Author, Book, Stock
# Register your models here.
class NoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Author)
admin.site.register(Book)

@admin.register(Stock)
class StockAdmin(NoDeleteAdminMixin, admin.ModelAdmin):
    pass
