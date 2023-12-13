from django.shortcuts import render
from add_blog.models import Blog
from category.models import Category
def home(request, category_slug = None):
    data = Blog.objects.all()
    if category_slug is not None:
        print(category_slug)
        ctg_slg = Category.objects.get(slug = category_slug)
        print(ctg_slg)
        data = Blog.objects.filter(category = ctg_slg)
        print(data)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'categories': categories})