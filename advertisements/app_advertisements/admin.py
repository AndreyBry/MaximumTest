from django.contrib import admin

from .models import Advertisement


# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'updated_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['action_auction_as_true', 'action_auction_as_false']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Добавить возможность торга')
    def action_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def action_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Advertisement, AdvertisementAdmin)
