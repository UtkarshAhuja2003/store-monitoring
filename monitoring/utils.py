import random

def generate_report(store_id):
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