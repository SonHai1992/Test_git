from django.urls import path
from .import views


urlpatterns = [
    path('', views.index),
    path('add/', views.AddQuestion, name='add'),
    path('edit/<int:id_input>', views.EditQuestion, name='edit'),
    path('delete/<int:id_input>', views.DeleteQuestion, name='delete'),
    path('list/', views.list),

    path('send_mail/', views.send_mail_view, name="send_mail"),

]
