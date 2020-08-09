from django.urls import path
from .views import tweet_detail_view, tweet_list_view


app_name = 'tweets'

urlpatterns = [
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path('tweets/', tweet_list_view),
]
