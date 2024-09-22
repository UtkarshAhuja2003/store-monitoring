from django.db import models

class store(models.Model):
    store_id = models.BigIntegerField(primary_key=True)
    timezone_str = models.CharField(max_length=100, default='America/Chicago')

class business_hours(models.Model):
    day_of_week = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()
    store_id = models.BigIntegerField()

class store_status(models.Model):
    store_id = models.BigIntegerField()
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=10)

class report(models.Model):
    store_id = models.BigIntegerField()
    uptime_last_hour = models.IntegerField()
    uptime_last_day = models.IntegerField()
    uptime_last_week = models.IntegerField()
    downtime_last_hour = models.IntegerField()
    downtime_last_day = models.IntegerField()
    downtime_last_week = models.IntegerField() 
