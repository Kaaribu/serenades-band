from django.contrib import admin
from my_band.models import Album, EndUser, Order, Image, Ticket

# Register your models here.
admin.site.register(Album)
admin.site.register(EndUser)
admin.site.register(Order)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('album', 'image_file')

admin.site.register(Image, ImagesAdmin)

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assignee')
    list_display = ('id', 'title', 'assignee', 'status', 'description', 'updated_at')
    search_fields = ('title', 'status')

admin.site.register(Ticket, TicketAdmin)