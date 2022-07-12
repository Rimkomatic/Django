from django.contrib import admin
from django.urls import path
from hello1 import views as hello1_view
from hello2 import views as hello2_view
from hello3 import views as hello3_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_h1',hello1_view.hello1_msg),
    path('hello_h2',hello2_view.hello2_msg),
    path('hello_h3',hello3_view.hello3_msg),
]
