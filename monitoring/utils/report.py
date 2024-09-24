from datetime import datetime
from django.utils import timezone
import random
from monitoring.utils.businessHours import getBusinessHours
from monitoring.utils.storeStatus import getStoreStatus, filter_statuses

def generate_report(store_id):
    print(getBusinessHours(store_id))
    
    date_threshold = timezone.make_aware(datetime(2023, 1, 25, 12, 0, 0))
    storeStatus = getStoreStatus(store_id, date_threshold)
    
    hourlyStatus = filter_statuses(storeStatus, "hour", date_threshold)
    dailyStatus = filter_statuses(storeStatus, "day", date_threshold)
    weeklyStatus = filter_statuses(storeStatus, "week", date_threshold)
    print(hourlyStatus[0].timestamp_utc, hourlyStatus[0].status)
    print(dailyStatus[0].timestamp_utc, dailyStatus[0].status)
    print(weeklyStatus[0].timestamp_utc, weeklyStatus[0].status)
    
    uptime_last_hour = random.randint(0, 60)
    uptime_last_day = random.randint(0, 24)
    downtime_last_hour = 60 - uptime_last_hour
    downtime_last_day = 24 - uptime_last_day
    
    return {
        'store_id': store_id,
        'uptime_last_hour': uptime_last_hour,
        'uptime_last_day': uptime_last_day,
        'downtime_last_hour': downtime_last_hour,
        'downtime_last_day': downtime_last_day,
        'uptime_last_week': uptime_last_day,
        'downtime_last_week': downtime_last_day,
    }
    


    
