from monitoring.models import store_status
from datetime import timedelta

def getStoreStatus(store_id, date_threshold):
    try:
        minDate = date_threshold - timedelta(weeks=1)

        status = store_status.objects.filter(store_id=store_id, timestamp_utc__gt=minDate, timestamp_utc__lt=date_threshold)

        return list(status)
    except Exception as e:
        print(e)
        return None
    
def filter_statuses(statuses, timeInterval, date_threshold):

    if timeInterval == "hour":
        minDate = date_threshold - timedelta(hours=1)
    elif timeInterval == "day":
        minDate = date_threshold - timedelta(days=1)
    elif timeInterval == "week":
        minDate = date_threshold - timedelta(weeks=1)

    return [status for status in statuses if minDate <= status.timestamp_utc <= date_threshold]
