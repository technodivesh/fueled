"""FUELED URL Configuration

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
from django.urls import path, include


from rest_framework import routers
from restaurant.api import views
from fldUser.api import views as UserView

from rest_framework_simplejwt import views as jwt_views
from FUELED import settings

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='api-restaurants')
router.register(r'reviews', views.ReviewViewSet, basename='api-reviews')
router.register(r'comments', views.CommentViewSet, basename='api-comments')
router.register(r'thumbdowns', views.ThumbDownViewSet, basename='api-thumbdown')
router.register(r'visited', views.VisitedViewSet, basename='api-visited')
router.register(r'user', UserView.UserViewSet, basename='api-user')
# router.register(r'users', UserView.UserViewSet, basename='api-users')
# router.register(r'user', UserView.UserViewSet, basename='api-user')
router.register(r'signup', UserView.SignUpViewSet, basename='api-register')
router.register(r'login', UserView.LoginViewSet, basename='api-login')
router.register(r'logout', UserView.LogOutViewSet, basename='api-logout')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('restaurant.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/restaurants', include('restaurant.api.urls', namespace='api-restaurants')),
    # path('api/users', include('fldUser.api.urls', namespace='api-restaurants')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

