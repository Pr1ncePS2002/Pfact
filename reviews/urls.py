from django.urls import path
from .views import ReviewCreateView, ProductReviewListView

urlpatterns = [
    path('', ProductReviewListView.as_view(), name='review-list'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
]
 
