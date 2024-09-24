from datetime import datetime
import pytz
from monitoring.models import store

def convertTimezoneUTC(time, store_id, dayOfWeek):
    timezone_str = getStoreTimezone(store_id)
    if(timezone_str == "UTC"):
        return time, dayOfWeek
    
    local_time = datetime.strptime(time, "%H:%M:%S")
    local_tz = pytz.timezone(timezone_str)
    arbitrary_monday = datetime(2024, 1, 1)
    local_datetime = local_tz.localize(datetime.combine(arbitrary_monday, local_time.time()))

    utc_datetime = local_datetime.astimezone(pytz.utc)

    utc_day_of_week = (dayOfWeek + (utc_datetime.date().weekday() - arbitrary_monday.weekday())) % 7

    return utc_datetime.strftime("%H:%M:%S"), utc_day_of_week
    
def getStoreTimezone(store_id):
    try:
        store_obj = store.objects.get(store_id=store_id)
        return store_obj.timezone_str
    except store.DoesNotExist:
        return "America/Chicago"