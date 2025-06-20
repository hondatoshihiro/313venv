"""
URL configuration for testapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from snippets.views import top

urlpatterns = [
    path('admin/', admin.site.urls),
    #自作Viewの追加
    #testapp01用
    #path('testapp01/', include('testapp01.urls')),
    #snippets用
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),    #snippets/urls.pyの読み込み
    path('accounts/', include('accounts.urls')),    #1.6.2
]
