from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('sprints', views.SprintViewSet)
router.register('tasks', views.TaskViewSet)
router.register('user', views.UserViewSet)



urlpatterns = [
                  path('gettoken/', obtain_auth_token),
                  path('', include(router.urls)),
                  path('movetask/', views.MoveTask.as_view(), name='movetask'),
                  path('changetask/', views.ChangeStatus.as_view(), name='changetask'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
