from django.contrib import admin
from my_band.models import Album, EndUser, Order, Image, Ticket

# Register your models here.
admin.site.register(Album)
admin.site.register(EndUser)
admin.site.register(Order)


class ImagesAdmin(admin.ModelAdmin):
    """Admin class for the Image model

       This class is used to display the Image model in the admin interface

       Attributes:
              list_display (tuple): A tuple of strings that are the names of the fields to display in the admin
              interface. The fields are displayed in the order they are listed in the tuple.
    """
    list_display = ('album', 'image_file')


admin.site.register(Image, ImagesAdmin)


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assignee')
    list_display = ('id', 'title', 'assignee', 'status', 'description', 'updated_at')
    search_fields = ('title', 'status')


admin.site.register(Ticket, TicketAdmin)