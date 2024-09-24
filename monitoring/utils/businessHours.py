from monitoring.models import business_hours
from monitoring.utils.timezone import convertTimezoneUTC

def getBusinessHours(store_id):
    try:
        businessHoursObject = business_hours.objects.filter(store_id=store_id)
        businessHours = [[] for _ in range(7)]
        
        for businessHour in businessHoursObject:
            UTCStartTime = convertTimezoneUTC(str(businessHour.start_time_local), store_id=store_id, dayOfWeek=businessHour.day_of_week)
            UTCEndTime = convertTimezoneUTC(str(businessHour.end_time_local), store_id=store_id, dayOfWeek=businessHour.day_of_week)

            start_time_str, start_day_of_week = UTCStartTime[0], UTCStartTime[1]
            end_time_str, end_day_of_week = UTCEndTime[0], UTCEndTime[1]
            
            if start_day_of_week == end_day_of_week:
                businessHours[start_day_of_week].append({start_time_str, end_time_str})
            else:
                businessHours[start_day_of_week].append({start_time_str, '23:59:59'})
                
                next_day_of_week = (start_day_of_week + 1) % 7
                businessHours[next_day_of_week].append({'00:00:00', end_time_str})

        return businessHours
    except business_hours.DoesNotExist:
        return None