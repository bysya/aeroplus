from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:customer_id>", views.customer, name="customer"),
    path("<int:customer_id>/<str:object_name>", views.object, name="object"),
    path("pdf/", views.spdf, name="pdf")
]
