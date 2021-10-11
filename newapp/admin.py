from django.contrib import admin
from .models import Market
# Register your models here.
class MarketAdmin(admin.ModelAdmin):
    list_display=['title','image','description','price']

admin.site.register(Market,MarketAdmin)
from .models import Market

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=("pk","title","description","created_at",)
    search_fields=("title")
    list_filter=("created_at")
admin.site.register(Market)