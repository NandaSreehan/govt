from django.urls import path
from notifications import views
urlpatterns=[
    path('notif',views.notes,name='notes')
]