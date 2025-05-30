from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from management.models import MenuItem

# View for menu page
def menu_view(request):
    menu = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu': menu})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_view, name='menu'),  # Homepage shows menu
]
