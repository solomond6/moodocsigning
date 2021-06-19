from django.db import models

# Create your models here.
class AppUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    supervisor = models.CharField(db_column='Supervisor', max_length=255)  # Field name made lowercase.
    forcechangepassword = models.IntegerField(db_column='ForceChangePassword')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    canchangecompany = models.IntegerField(db_column='CanChangeCompany')  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled')  # Field name made lowercase.
    defaultcompany = models.CharField(db_column='DefaultCompany', max_length=10)  # Field name made lowercase.
    previouscompany = models.CharField(db_column='PreviousCompany', max_length=10)  # Field name made lowercase.
    loginfailcount = models.IntegerField(db_column='LoginFailCount')  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='ModifiedDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recordversion = models.BigIntegerField(db_column='RecordVersion')  # Field name made lowercase.
    deleted = models.BigIntegerField(db_column='Deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_users'
        unique_together = (('username', 'deleted'),)
