from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver
from django.db.models import Avg

from apiApp.models import ProductRating, Review



@receiver(post_save, sender=Review)
def update_product_rating_on_save(sender, instance, **kwargs):
    product = instance.product 
    reviews = product.reviews.all()
    total_reviews = reviews.count() 

    review_average = reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0


    product_rating, created = ProductRating.objects.get_or_create(product=product)
    product_rating.average_rating = review_average 
    product_rating.total_reviews = total_reviews 
    product_rating.save()



@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    product = instance.product 
    reviews = product.reviews.all()
    total_reviews = reviews.count() 

    review_average = reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0


    product_rating, created = ProductRating.objects.get_or_create(product=product)
    product_rating.average_rating = review_average 
    product_rating.total_reviews = total_reviews 
    product_rating.save()