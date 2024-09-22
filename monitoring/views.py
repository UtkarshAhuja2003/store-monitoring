from django.http import JsonResponse
from .services import generateReport
from .models import report

def trigger_report(request, store_id):
    report_id = generateReport(store_id)
    return JsonResponse({'report_id': report_id})

def get_report(request, report_id):
    try:
        report_instance = report.objects.get(id=report_id)

        report_data = {
            'store_id': report_instance.store_id,
            'uptime_last_hour': report_instance.uptime_last_hour,
            'uptime_last_day': report_instance.uptime_last_day,
            'downtime_last_hour': report_instance.downtime_last_hour,
            'downtime_last_day': report_instance.downtime_last_day,
            'uptime_last_week': report_instance.uptime_last_week,
            'downtime_last_week': report_instance.downtime_last_week,
        }

        return JsonResponse({'status': 'Complete', 'report': report_data})
    except report.DoesNotExist:
        return JsonResponse({'status': 'Running'}, status=404)