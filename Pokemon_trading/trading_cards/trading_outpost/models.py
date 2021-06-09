from django.db import models
from datetime import datetime


# # Create your models here.

# class Card(models.Model):
#     name=models.CharField(max_length= 100)
#     card_type=models.ManyToManyField('Card_Type')
#     image=models.URLField(null=True)
#     rarety= models.IntegerField(default=0)
#     pokemon_id=models.IntegerField()
#     profile_connected= models.ManyToManyField(Profile, related_name='deck')

#     def __str__(self):
#         return self.name

# class Card_Type(models.Model):
#     name= models.CharField(max_length=100)
#     # card_type_id=models.IntegerField()
#     image= models.URLField(null=True)

#     def __str__(self):
#         return self.name


# class Transaction(models.Model):
#     STATUS_CHOICE= [
#         ('O','Open'),
#         ('C','Closed')
#     ]
#     card= models.ForeignKey(Card, on_delete=models.CASCADE)
#     giver= models.ForeignKey(Profile, on_delete=models.CASCADE)
#     status= models.CharField(choices= STATUS_CHOICES, default='O')
#     datetime= models.datetime.datetime.now()

# class Offer(models.Model):
#     STATUS_CHOICE= [
#         ('A', 'Accept'),
#         ('R', 'Refuse')
#     ]
#     card= models.ForeignKey(Card, on_delete=models.CASCADE)
#     getter= models.ForeignKey(Profile, on_delete=models.CASCADE)
#     status= models.CharField(choices= STATUS_CHOICES, default='O')
#     datetime= models.datetime.datetime.now()


class Queens(models.Model):
    name= models.CharField(max_length= 100)
    winner= models.BooleanField()
    missCongeniality= models.BooleanField()
    quote= models.TextField()
    image_url= models.URLField(null=True)

    def __str__(self):
        return self.name

class My_Card(models.Model):
    STATUS_CHOICE= [
        ('O','Open'),
        ('C','Closed'),
        ('G','Give')]
    queen= models.ForeignKey(Queens, on_delete=models.CASCADE) 
    #Should link the card object
    profile= models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    status= models.CharField(choices= STATUS_CHOICE, max_length=50, default='C')


# class Transaction(models.Model):
    
#     card= models.ForeignKey(My_Card, on_delete=models.CASCADE)
#     giver= models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
#     datetime= models.DateTimeField(auto_now_add=True)

#     def transaction_done(self):
#         return self.offer_set.filter(status='A')

class Offer(models.Model):

    card= models.ForeignKey(My_Card, on_delete=models.CASCADE)
    offerer= models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    datetime= models.DateTimeField(auto_now_add=True)

    # class Offer(models.Model):
    # STATUS_CHOICE= [
    #     ('A', 'Accept'),
    #     ('R', 'Refuse'),
    #     ('P','Pending')
    # ]
    # name= models.ForeignKey(My_Card, on_delete=models.CASCADE)
    # getter= models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    # status= models.CharField(choices= STATUS_CHOICE, max_length= 30, default='P')
    # datetime= models.DateTimeField(auto_now_add=True)


