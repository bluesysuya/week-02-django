from django.conf.urls import url
from . import views # 같은 폴더 내의 views 파일을 불러온다.

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
