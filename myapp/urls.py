# from django.urls import path
# from . import views
# from myproject.urls import urlpatterns

# urlpatterns = [
#     path('', views.index)
# ]

from django.contrib import admin
from django.urls import path, include

from .views import my_form_view, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Include myapp's URL patterns
]

from django.urls import path
from . import views  # Import your app's views

urlpatterns = [
    path('', views.index, name='index'),  # Example view for the app
    path('new/', views.new, name='new'),
    path('my_form/', my_form_view, name='my_form'),
    path('success/', success_view, name='success')

]
