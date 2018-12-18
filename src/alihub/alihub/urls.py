"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include



from rest_framework_jwt.views import obtain_jwt_token

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [


    url('admin/', admin.site.urls),


    url('accounts/', include('accounts.urls', namespace='accounts')),
    
    url('story/', include('story.urls', namespace='story')),

    url('comment/', include('comment.urls', namespace='comment')),

    url('profile/', include('userprofile.urls', namespace='profile')),

    url('review/', include('review.urls', namespace='review')),

    url('product/', include('product.urls', namespace='product')),

    url('category/', include('category.urls', namespace='category')),

    url('like/', include('like.urls', namespace='like')),

    url(r'^api/login/', obtain_jwt_token),

    url(r'^api/auth/', include('rest_framework.urls')),

    url(r'^auth/', include('rest_auth.urls')),
    
    url(r'^auth/registration/', include('rest_auth.registration.urls'))
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
