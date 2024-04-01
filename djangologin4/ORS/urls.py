from django.urls import path
from ORS import views

urlpatterns = [
    path("",views.index),
    # path('<page>/', views.action),
    # path('<page>/<operation>/<int:id>', views.actionId),
    path("Welcome/",views.Welcome),
    path("LoginView/",views.LoginView)

]