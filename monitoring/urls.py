from django.urls import path
from .views import trigger_report, get_report

urlpatterns = [
    path("trigger_report/<store_id>/", trigger_report),
    path("get_report/<report_id>/", get_report),
]
