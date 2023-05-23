"""
URL configuration for volunteer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("users/list/", views.users_list),
    path("users/list/<str:role>", views.users_list),
    path("users/create/", views.user_create),
    path("users/<int:id>/edit/", views.edit_user),
    path("users/<int:id>/view/", views.view_user),
    path("events/list/", views.events_list),
    path("events/<int:id>/view/", views.events_view),

    path("events/<int:id>/accept/<int:user>", views.event_accept_user),
    path("events/<int:id>/reject/<int:user>", views.event_reject_user),
    path("events/<int:id>/add/<int:user>", views.event_add_user),
    path("events/<int:id>/export", views.event_export),
    path("building/list/", views.building_list),
    path("building/add/", views.add_building),
    path("events/list/<str:search>", views.events_list),
    path("events/create/", views.event_create),

    path("classroom/create/", views.create_classroom),
    path("events/", views.events),
    path("events/<int:id>/invite", views.invite_classroom_event),

    path("classroom/invite/create/", views.create_invite),
    path("classroom/invite/update/", views.update_invite),
    path("classroom/invite/<uuid:classroom>/", views.invite),
    path("classroom/students/", views.classroom_students),

    path("classroom/student/<int:user>/view", views.classroom_view_student),

    path("events/<int:event>/request", views.event_request),
    path("my/events/", views.my_events),

    path('notifications/read/', views.read_notifications),
    path('notifications/list/', views.list_notifications)
    #path("classroom/student/<int:user>/delete", views.classroom_delete_student),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = views.handler500
