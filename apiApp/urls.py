from django.urls import path 
from . import views  



urlpatterns = [
    path("product_list", views.product_list, name="product_list"),
    path("products/<slug:slug>", views.product_detail, name="product_detail"),
    path("category_list", views.category_list, name="category_list"),
    path("category/<slug:slug>", views.category_detail, name="category_detail"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("update_cartitem_quantity/", views.update_cartitem_quantity, name="update_cartitem_quantity"),
    path("add_review/", views.add_review, name="add_review"),
    path("update_review/<int:pk>/", views.update_review, name="update_review"),
    path("delete_review/<int:pk>/", views.delete_review, name="delete_review"),
    path("delete_cartitem/<int:pk>/", views.delete_cartitem, name="delete_cartitem"),
    path("add_to_wishlist/", views.add_to_wishlist, name="add_to_wishlist"),
    path("search", views.product_search, name="search")
]