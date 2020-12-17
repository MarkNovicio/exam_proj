from django.urls import path

from . import views

urlpatterns = [
    path('success', views.success),
    path('quotes', views.read_quotes),
    path('quotes/create', views.create_quote),
    path('quotes/<int:quote_id>', views.quote_profile),
    path('quotes/<int:quote_id>/delete', views.delete_quote),
    path('quotes/<int:quote_id>/edit', views.edit_quote),
    path('users/<int:user_id>', views.user_profile),
    path('quotes/<int:quote_id>/favorite', views.favorite_quote),
    path('quotes/<int:quote_id>/unfavorite', views.unfavorite_quote)
    
]
