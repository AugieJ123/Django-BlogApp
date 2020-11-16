from django.urls import path
from . import  views

# Declaring app name helps to make url by application
app_name = 'blog_app'

urlpatterns = [
    # post view
    path('', views.post_list, name='post_list'), 
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name = 'post_detail')
]