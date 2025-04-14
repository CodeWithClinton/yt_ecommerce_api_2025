from django.urls import path 
from . import views  



urlpatterns = [
    path("product_list", views.product_list, name="product_list"),
    path("products/<slug:slug>", views.product_detail, name="product_detail"),
    path("category_list", views.category_list, name="category_list"),
    path("categories/<slug:slug>", views.category_detail, name="category_detail"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("update_cartitem_quantity/", views.update_cartitem_quantity, name="update_cartitem_quantity"),
    path("add_review/", views.add_review, name="add_review"),
    path("update_review/<int:pk>/", views.update_review, name="update_review"),
    path("delete_review/<int:pk>/", views.delete_review, name="delete_review"),
    path("delete_cartitem/<int:pk>/", views.delete_cartitem, name="delete_cartitem"),
    path("add_to_wishlist/", views.add_to_wishlist, name="add_to_wishlist"),
    path("search", views.product_search, name="search"),

    path("create_checkout_session/", views.create_checkout_session, name="create_checkout_session"),
    path("webhook/", views.my_webhook_view, name="webhook"),

    # Newly Added

    path("get_orders", views.get_orders, name="get_orders"),
    path("create_user/", views.create_user, name="create_user"),
    path("existing_user/<str:email>", views.existing_user, name="existing_user"),
    path("add_address/", views.add_address, name="add_address"),
    path("get_address", views.get_address, name="get_address"),
    path("my_wishlists", views.my_wishlists, name="my_wishlists"),
    path("product_in_wishlist", views.product_in_wishlist, name="product_in_wishlist"),
    path("get_cart/<str:cart_code>", views.get_cart, name="get_cart"),
    path("get_cart_stat", views.get_cart_stat, name="get_cart_stat"),
    path("product_in_cart", views.product_in_cart, name="product_in_cart")



]