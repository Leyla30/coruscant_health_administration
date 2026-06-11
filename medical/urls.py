from django.urls import path

from . import views


urlpatterns = [
    path(
        "reading/",
        views.add_health_reading,
        name="add_health_reading"
    ),

    path(
        "report/",
        views.create_report,
        name="create_report"
    ),

    path(
        "order/",
        views.create_order,
        name="create_order"
    ),

    path(
        "result/",
        views.add_result,
        name="add_result"
    ),
]