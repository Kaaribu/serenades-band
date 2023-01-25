from django.db import models

# Create your models here.
# set a default value for the title field


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.artist + ' - ' + self.genre

class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)



class EndUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.phone + ' - ' + self.address


class TicketsStatus(models.Model):
    choices = None
    to_do = 'To do'
    in_progress = 'In progress'
    in_review = 'In review'
    done = 'Done'


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(EndUser, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=TicketsStatus.choices, default=TicketsStatus.to_do)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(EndUser, on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateField(auto_now_add=True, null=True)
    quantity = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date_ordered')









