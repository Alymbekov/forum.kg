from django.shortcuts import render
from apps.category.models import Category

#получаем все обЪекты категориев на странице 
def get_category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', locals())