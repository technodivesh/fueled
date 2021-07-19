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

from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers
from restaurant.api import views
from fldUser.api import views as UserView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt import views as jwt_views
from fldUser.api.views import CustomTokenObtainPairView

# from FUELED import settings

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='api-restaurants')
router.register(r'reviews', views.ReviewViewSet, basename='api-reviews')
router.register(r'comments', views.CommentViewSet, basename='api-comments')
router.register(r'thumbdowns', views.ThumbDownViewSet, basename='api-thumbdown')
router.register(r'visited', views.VisitedViewSet, basename='api-visited')
router.register(r'user', UserView.UserViewSet, basename='api-user')
# router.register(r'users', UserView.UserViewSet, basename='api-users')
# router.register(r'user', UserView.UserViewSet, basename='api-user')
router.register(r'register', UserView.RegisterViewSet, basename='api-register')
# router.register(r'login', UserView.LoginViewSet, basename='api-login')
# router.register(r'logout', UserView.LogOutViewSet, basename='api-logout')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include('restaurant.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema', get_schema_view(
        title="RestaurantAPI",
        description="API for the Restaurant Recommendation",
        url='http://localhost/api/schema',
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', include_docs_urls(title='RestaurantAPI')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


