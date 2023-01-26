from django.db import models

# Create your models here.
# set a default value for the title field


class Album(models.Model):
    """
    Class Album(models.Model) represents an album of a music band.

    Attributes:
    id (AutoField): the id of the album
    title (CharField): The name of the album.
    artist (CharField): The name of the artist.
    genre (CharField): The genre of the album.
    release_date (DateField): The release date of the album.
    price (DecimalField): The price of the album.
    is_favorite (BooleanField): Whether the album is a favorite or not.

    Methods:
    str(self): Returns the name of the album as a string.
    """
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
    """
    Class Image(models.Model) represents an image of an album.

    Attributes:
        album (ForeignKey): The album that the image belongs to.
        image_file (ImageField): The image of the album.
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)


class EndUser(models.Model):
    """
        Class EndUser(models.Model) represents an end user of the website.

       Attributes:
           name (CharField): The name of the end user.
           email (EmailField): The email of the end user.
           phone (CharField): The phone number of the end user.
           address (CharField): The address of the end user.

       Methods:
           str(self): Returns the name of the end user as a string.
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.phone + ' - ' + self.address


class TicketsStatus(models.Model):
    """
        Class TicketsStatus(models.Model) represents the status of a ticket.

        Attributes:
            choices (CharField): The status of the ticket.
            to_do (BooleanField): Whether the ticket is to do or not.
            in_progress (BooleanField): Whether the ticket is in progress or not.
            in_review (BooleanField): Whether the ticket is in review or not.
            done (BooleanField): Whether the ticket is done or not.
    """
    choices = None
    to_do = 'To do'
    in_progress = 'In progress'
    in_review = 'In review'
    done = 'Done'


class Ticket(models.Model):
    """
        Class Ticket(models.Model) represents a ticket.

        Attributes:
            title (CharField): The title of the ticket.
            assignee (ForeignKey): The assignee of the ticket.
            status (CharField): The status of the ticket.
            description (CharField): The description of the ticket.
            created_at (DateTimeField): The date and time the ticket was created.
            updated_at (DateTimeField): The date and time the ticket was updated.
    """
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(EndUser, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=TicketsStatus.choices, default=TicketsStatus.to_do)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)


class Order(models.Model):
    """
        Class Order(models.Model) represents an order.

        Attributes:
            user (ForeignKey): The user that made the order.
            album (ForeignKey): The album that was ordered.
            date_ordered (DateTimeField): The date and time the order was made.
            quantity (IntegerField): The quantity of the album that was ordered.
            is_complete (BooleanField): Whether the order is complete or not.

        Methods:
            place_order(self): Saves the order.
            get_orders_by_customer(self, customer_id): Returns the orders of a customer.
    """
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









