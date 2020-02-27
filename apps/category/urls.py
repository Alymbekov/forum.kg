from django.urls import path
from apps.category.views import get_category_list

urlpatterns = [
    path('categories/', get_category_list, name='categories'),
]
