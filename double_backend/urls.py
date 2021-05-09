"""double_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import double_backend.views as views
import double_backend.models as models
from double_backend.views import get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/',
         get_all(models.Category)),
    path('levels/',
         get_all(models.Level)),
    path('themes/',
         get_all(models.Theme)),
    path('themes/<int:theme_id>/',
         views.get_theme),
    path('words/<int:word_id>/',
         views.get_word),
    path('media/<path:file_path>/',
         views.get_file)
]
