from django.urls import path
from bookapp.views import BookShelfView

urlpatterns = [
    path('',BookShelfView.as_view() ),
]
