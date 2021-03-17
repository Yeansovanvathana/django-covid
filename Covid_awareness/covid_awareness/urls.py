"""covid_awareness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webpages.views import hospital_detail,homepage,signin,symtoms_analysis,signup,signout,profile
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('signin/',signin),
    path('signup/',signup),
    path('hospital/',hospital_detail),
    path('symtoms-analysis/',symtoms_analysis),
    path('signout/',signout),
    path('profile/',profile),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
