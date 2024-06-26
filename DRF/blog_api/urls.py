from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detalcreate'),
    path('', PostList.as_view(), name='listcreate'),
]