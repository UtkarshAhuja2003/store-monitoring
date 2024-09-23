from .utils import generate_report
from .models import report

def generateReport(store_id):
    try:
        report_data = generate_report(store_id)

        Report = report(
            store_id=store_id,
            uptime_last_hour=report_data['uptime_last_hour'],
            uptime_last_day=report_data['uptime_last_day'],
            downtime_last_hour=report_data['downtime_last_hour'],
            downtime_last_day=report_data['downtime_last_day'],
            uptime_last_week=report_data['uptime_last_week'],
            downtime_last_week=report_data['downtime_last_week']
        )
        Report.save()

        return Report.id
    except Exception as e:
        return str(e)
