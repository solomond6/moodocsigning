# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, time, timedelta
from django.utils import timezone


class AppApprovals(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    approvalsetupdetailid = models.BigIntegerField(db_column='ApprovalSetupDetailID')  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    recordid = models.BigIntegerField(db_column='RecordID')  # Field name made lowercase.
    approvalsno = models.IntegerField(db_column='ApprovalSNo')  # Field name made lowercase.
    approvalname = models.CharField(db_column='ApprovalName', max_length=255)  # Field name made lowercase.
    approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=255)  # Field name made lowercase.
    approvalstatusreason = models.TextField(db_column='ApprovalStatusReason')  # Field name made lowercase.
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
        db_table = 'app_approvals'


class AppApprovalsetup(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    approvalsno = models.IntegerField(db_column='ApprovalSNo')  # Field name made lowercase.
    approvalname = models.CharField(db_column='ApprovalName', max_length=255)  # Field name made lowercase.
    eligiglerecordsquery = models.CharField(db_column='EligigleRecordsQuery', max_length=255)  # Field name made lowercase.
    approverusersquery = models.CharField(db_column='ApproverUsersQuery', max_length=255)  # Field name made lowercase.
    autoapprove = models.IntegerField(db_column='AutoApprove')  # Field name made lowercase.
    autoapprovalstatus = models.CharField(db_column='AutoApprovalStatus', max_length=255)  # Field name made lowercase.
    autoapprovalreason = models.TextField(db_column='AutoApprovalReason')  # Field name made lowercase.
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
        db_table = 'app_approvalsetup'


class AppAssemblies(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    assemblyname = models.CharField(db_column='AssemblyName', max_length=512)  # Field name made lowercase.
    viewfilelocation = models.TextField(db_column='ViewFileLocation')  # Field name made lowercase.
    reportfilelocation = models.TextField(db_column='ReportFileLocation')  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_assemblies'
        unique_together = (('assemblyname', 'machinename', 'deleted'),)


class AppBatchinfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    runnableclassname = models.CharField(db_column='RunnableClassName', max_length=255)  # Field name made lowercase.
    runnablecaption = models.CharField(db_column='RunnableCaption', max_length=255)  # Field name made lowercase.
    alerts = models.IntegerField(db_column='Alerts')  # Field name made lowercase.
    serializedobject = models.TextField(db_column='SerializedObject')  # Field name made lowercase.
    lastrundatetime = models.DateTimeField(db_column='LastRunDateTime')  # Field name made lowercase.
    proposedstartdatetime = models.DateTimeField(db_column='ProposedStartDateTime')  # Field name made lowercase.
    nextproposedrundatetime = models.DateTimeField(db_column='NextProposedRunDateTime')  # Field name made lowercase.
    recurrenceperiod = models.CharField(db_column='RecurrencePeriod', max_length=255)  # Field name made lowercase.
    recurrenceperiodgap = models.IntegerField(db_column='RecurrencePeriodGap')  # Field name made lowercase.
    maxrecurrencecount = models.IntegerField(db_column='MaxRecurrenceCount')  # Field name made lowercase.
    recurrencecount = models.IntegerField(db_column='RecurrenceCount')  # Field name made lowercase.
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
        db_table = 'app_batchinfo'


class AppBatchruninfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batchinfoid = models.BigIntegerField(db_column='BatchInfoID')  # Field name made lowercase.
    runnableclassname = models.CharField(db_column='RunnableClassName', max_length=255)  # Field name made lowercase.
    runnablecaption = models.CharField(db_column='RunnableCaption', max_length=255)  # Field name made lowercase.
    proposedstartdatetime = models.DateTimeField(db_column='ProposedStartDateTime')  # Field name made lowercase.
    actualstartdatetime = models.DateTimeField(db_column='ActualStartDateTime')  # Field name made lowercase.
    progress = models.DecimalField(db_column='Progress', max_digits=64, decimal_places=30)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    exitcode = models.IntegerField(db_column='ExitCode')  # Field name made lowercase.
    infologdata = models.TextField(db_column='InfologData')  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID')  # Field name made lowercase.
    printarchiveid = models.BigIntegerField(db_column='PrintArchiveID')  # Field name made lowercase.
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
        db_table = 'app_batchruninfo'


class AppBranch(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_branch'
        unique_together = (('name', 'company', 'deleted'), ('branchid', 'company', 'deleted'),)


class AppCompanies(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyID', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_companies'
        unique_together = (('companyid', 'deleted'),)


class AppCompanyInfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyID', max_length=10)  # Field name made lowercase.
    smtphost = models.CharField(db_column='SMTPHost', max_length=255)  # Field name made lowercase.
    smtpport = models.IntegerField(db_column='SMTPPort')  # Field name made lowercase.
    smtpoutgoingemail = models.CharField(db_column='SMTPOutgoingEmail', max_length=255)  # Field name made lowercase.
    smtpoutgoingemailname = models.CharField(db_column='SMTPOutgoingEmailName', max_length=255)  # Field name made lowercase.
    smtpusername = models.CharField(db_column='SMTPUsername', max_length=255)  # Field name made lowercase.
    smtppassword = models.CharField(db_column='SMTPPassword', max_length=255)  # Field name made lowercase.
    usesslforsmtp = models.IntegerField(db_column='UseSSLForSMTP')  # Field name made lowercase.
    logopath = models.TextField(db_column='LogoPath')  # Field name made lowercase.
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
        db_table = 'app_company_info'
        unique_together = (('companyid', 'deleted'),)


class AppDatabaselog(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    entityid = models.BigIntegerField(db_column='EntityID')  # Field name made lowercase.
    logtype = models.CharField(db_column='LogType', max_length=255)  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
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
        db_table = 'app_databaselog'


class AppDatabaselogsetup(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    logtype = models.CharField(db_column='LogType', max_length=255)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_databaselogsetup'
        unique_together = (('entityname', 'logtype', 'field', 'deleted'),)


class AppDocumenthandling(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    entityid = models.BigIntegerField(db_column='EntityID')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
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
        db_table = 'app_documenthandling'


class AppDocumenthandlingdocuments(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    documenthandlingid = models.BigIntegerField(db_column='DocumentHandlingID')  # Field name made lowercase.
    documentblob = models.TextField(db_column='DocumentBlob')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_documenthandlingdocuments'
        unique_together = (('documenthandlingid', 'company', 'deleted'),)


class AppEntitypermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
    defaultformpermission = models.CharField(db_column='DefaultFormPermission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_entitypermissions'
        unique_together = (('entityname', 'deleted'),)


class AppFailedlogins(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    server = models.CharField(db_column='Server', max_length=255)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=255)  # Field name made lowercase.
    logondatetime = models.DateTimeField(db_column='LogOnDateTime')  # Field name made lowercase.
    clientip = models.CharField(db_column='ClientIP', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_failedlogins'


class AppFieldpermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_fieldpermissions'
        unique_together = (('entityname', 'fieldname', 'deleted'),)


class AppFormcontrolpermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=255)  # Field name made lowercase.
    operationcontrolid = models.CharField(db_column='OperationControlId', max_length=255)  # Field name made lowercase.
    operationid = models.CharField(db_column='OperationId', max_length=255)  # Field name made lowercase.
    operationtitle = models.CharField(db_column='OperationTitle', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_formcontrolpermissions'
        unique_together = (('formname', 'operationcontrolid', 'operationid', 'deleted'),)


class AppLicense(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    assemblyname = models.CharField(db_column='AssemblyName', max_length=512)  # Field name made lowercase.
    licensedata = models.TextField(db_column='LicenseData')  # Field name made lowercase.
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
        db_table = 'app_license'
        unique_together = (('assemblyname', 'deleted'),)


class AppNavigationpermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    navigationid = models.CharField(db_column='NavigationID', max_length=500)  # Field name made lowercase.
    navigationcaption = models.CharField(db_column='NavigationCaption', max_length=1024)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_navigationpermissions'
        unique_together = (('navigationid', 'company', 'deleted'),)


class AppNumbersequences(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sequenceid = models.CharField(db_column='SequenceId', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255)  # Field name made lowercase.
    currentnum = models.BigIntegerField(db_column='CurrentNum')  # Field name made lowercase.
    holdduringtransaction = models.IntegerField(db_column='HoldDuringTransaction')  # Field name made lowercase.
    fetchaheadnumber = models.IntegerField(db_column='FetchAheadNumber')  # Field name made lowercase.
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
        db_table = 'app_numbersequences'
        unique_together = (('sequenceid', 'company', 'deleted'),)


class AppOnlineusers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    server = models.CharField(db_column='Server', max_length=255)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=255)  # Field name made lowercase.
    logondatetime = models.DateTimeField(db_column='LogOnDateTime')  # Field name made lowercase.
    clientip = models.CharField(db_column='ClientIP', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_onlineusers'


class AppPermissiongrouppermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
    accesslevel = models.CharField(db_column='AccessLevel', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_permissiongrouppermissions'
        unique_together = (('groupname', 'permission', 'deleted'),)


class AppPermissiongroups(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=255)  # Field name made lowercase.
    autocreated = models.IntegerField(db_column='AutoCreated')  # Field name made lowercase.
    onepertime = models.IntegerField(db_column='OnePerTime')  # Field name made lowercase.
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
        db_table = 'app_permissiongroups'
        unique_together = (('groupname', 'deleted'),)


class AppPermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_permissions'
        unique_together = (('permission', 'deleted'),)


class AppPrintarchive(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=255)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='ReportTitle', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_printarchive'


class AppPrintarchivedata(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    printarchiveid = models.BigIntegerField(db_column='PrintArchiveID')  # Field name made lowercase.
    reportblob = models.TextField(db_column='ReportBlob')  # Field name made lowercase.
    printfileformat = models.CharField(db_column='PrintFileFormat', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_printarchivedata'
        unique_together = (('printarchiveid', 'company', 'deleted'),)


class AppQueries(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    ownerform = models.CharField(db_column='OwnerForm', max_length=255)  # Field name made lowercase.
    queryblob = models.TextField(db_column='QueryBlob')  # Field name made lowercase.
    userquery = models.IntegerField(db_column='UserQuery')  # Field name made lowercase.
    public = models.IntegerField(db_column='Public')  # Field name made lowercase.
    allowmerge = models.IntegerField(db_column='AllowMerge')  # Field name made lowercase.
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
        db_table = 'app_queries'
        unique_together = (('name', 'deleted'),)


class AppRecordlevelsecuritypermissiongroupassignments(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    permissiongroup = models.CharField(db_column='PermissionGroup', max_length=255)  # Field name made lowercase.
    recordlevelsecurityname = models.CharField(db_column='RecordLevelSecurityName', max_length=255)  # Field name made lowercase.
    crosscomp = models.IntegerField(db_column='CrossComp')  # Field name made lowercase.
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
        db_table = 'app_recordlevelsecuritypermissiongroupassignments'
        unique_together = (('permissiongroup', 'recordlevelsecurityname', 'deleted'),)


class AppReportredirection(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    originalreportlocation = models.CharField(db_column='OriginalReportLocation', max_length=255)  # Field name made lowercase.
    redirectedreportlocation = models.CharField(db_column='RedirectedReportLocation', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_reportredirection'
        unique_together = (('originalreportlocation', 'company', 'deleted'),)


class AppRunnablepermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_runnablepermissions'
        unique_together = (('formname', 'deleted'),)


class AppSavedreports(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='ReportTitle', max_length=255)  # Field name made lowercase.
    serializedobject = models.TextField(db_column='SerializedObject')  # Field name made lowercase.
    public = models.IntegerField(db_column='Public')  # Field name made lowercase.
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
        db_table = 'app_savedreports'
        unique_together = (('createdby', 'reporttitle', 'company', 'deleted'),)


class AppSystemparameters(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maxloginattempts = models.IntegerField(db_column='MaxLoginAttempts')  # Field name made lowercase.
    helpsiteurl = models.TextField(db_column='HelpSiteUrl')  # Field name made lowercase.
    usermustchangepasswordonfirstlogin = models.IntegerField(db_column='UserMustChangePasswordOnFirstLogin')  # Field name made lowercase.
    acceptablepasswordregex = models.CharField(db_column='AcceptablePasswordRegex', max_length=255)  # Field name made lowercase.
    acceptablepassworddescription = models.TextField(db_column='AcceptablePasswordDescription')  # Field name made lowercase.
    usetwofactorauthentication = models.CharField(db_column='UseTwoFactorAuthentication', max_length=255)  # Field name made lowercase.
    userbrowserfingerprintexpiryminutes = models.IntegerField(db_column='UserBrowserFingerprintExpiryMinutes')  # Field name made lowercase.
    twofactortokenexpiryminutes = models.IntegerField(db_column='TwoFactorTokenExpiryMinutes')  # Field name made lowercase.
    defaultformaccesslevel = models.CharField(db_column='DefaultFormAccessLevel', max_length=255)  # Field name made lowercase.
    defaultdataformaccesslevel = models.CharField(db_column='DefaultDataFormAccessLevel', max_length=255)  # Field name made lowercase.
    defaultentityaccesslevel = models.CharField(db_column='DefaultEntityAccessLevel', max_length=255)  # Field name made lowercase.
    defaultfieldaccesslevel = models.CharField(db_column='DefaultFieldAccessLevel', max_length=255)  # Field name made lowercase.
    defaultreportaccesslevel = models.CharField(db_column='DefaultReportAccessLevel', max_length=255)  # Field name made lowercase.
    defaultrunnableaccesslevel = models.CharField(db_column='DefaultRunnableAccessLevel', max_length=255)  # Field name made lowercase.
    defaultoperationaccesslevel = models.CharField(db_column='DefaultOperationAccessLevel', max_length=255)  # Field name made lowercase.
    defaultmenuaccesslevel = models.CharField(db_column='DefaultMenuAccessLevel', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_systemparameters'


class AppUseralerts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    alertid = models.BigIntegerField(db_column='AlertID')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    entityid = models.BigIntegerField(db_column='EntityID')  # Field name made lowercase.
    changetype = models.CharField(db_column='ChangeType', max_length=255)  # Field name made lowercase.
    alerttitle = models.CharField(db_column='AlertTitle', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    read = models.IntegerField(db_column='Read')  # Field name made lowercase.
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
        db_table = 'app_useralerts'


class AppUseralertsetup(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=255)  # Field name made lowercase.
    changetype = models.CharField(db_column='ChangeType', max_length=255)  # Field name made lowercase.
    entityid = models.BigIntegerField(db_column='EntityID')  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=255)  # Field name made lowercase.
    forallsubordinates = models.IntegerField(db_column='ForAllSubordinates')  # Field name made lowercase.
    alerttitle = models.CharField(db_column='AlertTitle', max_length=255)  # Field name made lowercase.
    criteria = models.TextField(db_column='Criteria')  # Field name made lowercase.
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
        db_table = 'app_useralertsetup'


class AppUserbrowserfingerprinthashes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=255)  # Field name made lowercase.
    fingerprinthash = models.CharField(db_column='FingerprintHash', max_length=255)  # Field name made lowercase.
    expirydatetime = models.DateTimeField(db_column='ExpiryDateTime')  # Field name made lowercase.
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
        db_table = 'app_userbrowserfingerprinthashes'


class AppUserlogintokens(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=255)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=255)  # Field name made lowercase.
    expirydatetime = models.DateTimeField(db_column='ExpiryDateTime')  # Field name made lowercase.
    used = models.IntegerField(db_column='Used')  # Field name made lowercase.
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
        db_table = 'app_userlogintokens'


class AppUserpermissiongroups(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    usergroup = models.CharField(db_column='UserGroup', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_userpermissiongroups'
        unique_together = (('username', 'usergroup', 'deleted'),)


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


class AppUsersettings(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', max_length=255)  # Field name made lowercase.
    parentobject = models.CharField(db_column='ParentObject', max_length=255)  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
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
        db_table = 'app_usersettings'
        unique_together = (('username', 'objectname', 'parentobject', 'deleted'),)


class AppWebservicepermissions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    webservicename = models.CharField(db_column='WebServiceName', max_length=255)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=255)  # Field name made lowercase.
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
        db_table = 'app_webservicepermissions'
        unique_together = (('webservicename', 'company', 'deleted'),)


class Applicantfingerprintdata(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    fingerprintimagedata = models.TextField(db_column='FingerprintImageData')  # Field name made lowercase.
    fingerprintminutiaedata = models.TextField(db_column='FingerprintMinutiaeData')  # Field name made lowercase.
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
        db_table = 'applicantfingerprintdata'
        unique_together = (('refno', 'company', 'deleted'),)


class Applicationpassports(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    passportdata = models.TextField(db_column='PassportData')  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=255)  # Field name made lowercase.
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
        db_table = 'applicationpassports'
        unique_together = (('refno', 'company', 'deleted'),)


class Applicationresultremark(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    applicationresultremarkid = models.CharField(db_column='ApplicationResultRemarkID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    default = models.IntegerField(db_column='Default')  # Field name made lowercase.
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
        db_table = 'applicationresultremark'
        unique_together = (('applicationresultremarkid', 'company', 'deleted'),)


class Applications(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=255)  # Field name made lowercase.
    nametitle = models.CharField(db_column='NameTitle', max_length=255)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=255)  # Field name made lowercase.
    bvn = models.CharField(db_column='BVN', max_length=255)  # Field name made lowercase.
    educationallevel = models.CharField(db_column='EducationalLevel', max_length=255)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255)  # Field name made lowercase.
    stateoforigin = models.CharField(db_column='StateOfOrigin', max_length=255)  # Field name made lowercase.
    localgovernmentarea = models.CharField(db_column='LocalGovernmentArea', max_length=255)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255)  # Field name made lowercase.
    postaladdress = models.TextField(db_column='PostalAddress')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    lgaofresidence = models.CharField(db_column='LGAofResidence', max_length=255)  # Field name made lowercase.
    lcdaofresidence = models.CharField(db_column='LCDAofResidence', max_length=255)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=255)  # Field name made lowercase.
    maidenname = models.CharField(db_column='MaidenName', max_length=255)  # Field name made lowercase.
    nextofkinname = models.CharField(db_column='NextOfKinName', max_length=255)  # Field name made lowercase.
    addressofnextofkin = models.TextField(db_column='AddressOfNextOfKin')  # Field name made lowercase.
    nextofkinrelationship = models.CharField(db_column='NextOfKinRelationship', max_length=255)  # Field name made lowercase.
    nextofkinoccupation = models.CharField(db_column='NextOfKinOccupation', max_length=255)  # Field name made lowercase.
    nextofkintelephonenumber = models.CharField(db_column='NextOfKinTelephoneNumber', max_length=255)  # Field name made lowercase.
    driverlicensenumber = models.CharField(db_column='DriverLicenseNumber', max_length=255)  # Field name made lowercase.
    driverlicenseexpirydate = models.DateField(db_column='DriverLicenseExpiryDate')  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=64, decimal_places=30)  # Field name made lowercase.
    approved = models.IntegerField(db_column='Approved')  # Field name made lowercase.
    submittedforapproval = models.IntegerField(db_column='SubmittedForApproval')  # Field name made lowercase.
    scheduled = models.IntegerField(db_column='Scheduled')  # Field name made lowercase.
    blacklist = models.IntegerField(db_column='Blacklist')  # Field name made lowercase.
    applicationstatus = models.CharField(db_column='ApplicationStatus', max_length=255)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255)  # Field name made lowercase.
    remarkreason = models.CharField(db_column='RemarkReason', max_length=255)  # Field name made lowercase.
    firstapprovalrejectionreason = models.CharField(db_column='FirstApprovalRejectionReason', max_length=255)  # Field name made lowercase.
    secondapprovalrejectionreason = models.CharField(db_column='SecondApprovalRejectionReason', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    uberscore = models.DecimalField(db_column='UberScore', max_digits=64, decimal_places=30)  # Field name made lowercase.
    uberid = models.CharField(db_column='UberID', max_length=255)  # Field name made lowercase.
    ubername = models.CharField(db_column='UberName', max_length=255)  # Field name made lowercase.
    approvedscheme = models.CharField(db_column='ApprovedScheme', max_length=255)  # Field name made lowercase.
    assignedvehicle = models.CharField(db_column='AssignedVehicle', max_length=255)  # Field name made lowercase.
    assignedvehicleregno = models.CharField(db_column='AssignedVehicleRegNo', max_length=255)  # Field name made lowercase.
    vehicleassignmentdatetime = models.DateTimeField(db_column='VehicleAssignmentDateTime')  # Field name made lowercase.
    assignedvehicledetails = models.CharField(db_column='AssignedVehicleDetails', max_length=255)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='ModifiedDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recordversion = models.BigIntegerField(db_column='RecordVersion')  # Field name made lowercase.
    deleted = models.BigIntegerField(db_column='Deleted')  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('drn', 'company', 'deleted'),)


class Autoscheduleexam(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationid = models.BigIntegerField(db_column='ExaminationID')  # Field name made lowercase.
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
        db_table = 'autoscheduleexam'
        unique_together = (('examinationid', 'company', 'deleted'),)


class Bank(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankid = models.CharField(db_column='BankID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    flutterwavecode = models.CharField(db_column='FlutterwaveCode', max_length=255)  # Field name made lowercase.
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
        db_table = 'bank'
        unique_together = (('bankid', 'company', 'deleted'), ('flutterwavecode', 'company', 'deleted'),)


class Bankdetails(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=255)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=255)  # Field name made lowercase.
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
        db_table = 'bankdetails'
        unique_together = (('drn', 'bank', 'accountnumber', 'company', 'deleted'),)


class Batches(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batchid = models.CharField(db_column='BatchID', max_length=255)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
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
        db_table = 'batches'
        unique_together = (('batchid', 'company', 'deleted'),)


class Countries(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.CharField(db_column='CountryID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255)  # Field name made lowercase.
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
        db_table = 'countries'
        unique_together = (('countryid', 'deleted'),)


class Dashboardreports(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    savedreportid = models.BigIntegerField(db_column='SavedReportID')  # Field name made lowercase.
    sno = models.BigIntegerField(db_column='SNo')  # Field name made lowercase.
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
        db_table = 'dashboardreports'
        unique_together = (('username', 'sno', 'company', 'deleted'), ('username', 'savedreportid', 'company', 'deleted'),)


class Dispatch(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dispatchid = models.CharField(db_column='DispatchID', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    lgv = models.CharField(db_column='LGV', max_length=255)  # Field name made lowercase.
    lcda = models.CharField(db_column='LCDA', max_length=255)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
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
        db_table = 'dispatch'
        unique_together = (('phone', 'company', 'deleted'), ('dispatchid', 'company', 'deleted'),)


class Dispatchoperationalarea(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dispatchid = models.CharField(db_column='DispatchID', max_length=255)  # Field name made lowercase.
    lga = models.CharField(db_column='LGA', max_length=255)  # Field name made lowercase.
    lcda = models.CharField(db_column='LCDA', max_length=255)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.
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
        db_table = 'dispatchoperationalarea'
        unique_together = (('dispatchid', 'lga', 'company', 'deleted'),)


class Dispatchschedule(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dispatchid = models.CharField(db_column='DispatchID', max_length=255)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed')  # Field name made lowercase.
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
        db_table = 'dispatchschedule'


class Dispatchscheduleparameters(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maxscheduleperdispatch = models.IntegerField(db_column='MaxSchedulePerDispatch')  # Field name made lowercase.
    dispatchschedulemode = models.CharField(db_column='DispatchScheduleMode', max_length=255)  # Field name made lowercase.
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
        db_table = 'dispatchscheduleparameters'


class Driverapprovalhistory(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.
    dispatchscheduleid = models.BigIntegerField(db_column='DispatchScheduleID')  # Field name made lowercase.
    firstapprovalstatus = models.CharField(db_column='FirstApprovalStatus', max_length=255)  # Field name made lowercase.
    firstapprovalstatusreason = models.CharField(db_column='FirstApprovalStatusReason', max_length=255)  # Field name made lowercase.
    secondapprovalstatus = models.CharField(db_column='SecondApprovalStatus', max_length=255)  # Field name made lowercase.
    secondapprovalstatusreason = models.CharField(db_column='SecondApprovalStatusReason', max_length=255)  # Field name made lowercase.
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
        db_table = 'driverapprovalhistory'
        unique_together = (('drn', 'guarantorid', 'dispatchscheduleid', 'company', 'deleted'),)


class Driverdocuments(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=255)  # Field name made lowercase.
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
        db_table = 'driverdocuments'
        unique_together = (('drn', 'documenttype', 'company', 'deleted'),)


class Driverdocumenttypes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    driverdocumenttype = models.CharField(db_column='DriverDocumentType', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    documentstatus = models.CharField(db_column='DocumentStatus', max_length=255)  # Field name made lowercase.
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
        db_table = 'driverdocumenttypes'
        unique_together = (('driverdocumenttype', 'company', 'deleted'),)


class Driverparameter(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    noofguarantor = models.IntegerField()
    driverscheme = models.CharField(max_length=255)
    guarantoroptionalforapprovalsubmission = models.IntegerField(db_column='GuarantorOptionalForApprovalSubmission')  # Field name made lowercase.
    guarantoroptionalforverfication = models.IntegerField(db_column='GuarantorOptionalForVerfication')  # Field name made lowercase.
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
        db_table = 'driverparameter'


class Driverschemes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schemeid = models.CharField(db_column='SchemeID', max_length=255)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    principal = models.IntegerField(db_column='Principal')  # Field name made lowercase.
    loanproductid = models.CharField(db_column='LoanProductId', max_length=255)  # Field name made lowercase.
    monthlypayment = models.DecimalField(db_column='MonthlyPayment', max_digits=64, decimal_places=30)  # Field name made lowercase.
    tenure = models.IntegerField(db_column='Tenure')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
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
        db_table = 'driverschemes'
        unique_together = (('schemeid', 'drn', 'company', 'deleted'),)


class Examinationcategories(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationid = models.BigIntegerField(db_column='ExaminationID')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    numberofquestions = models.IntegerField(db_column='NumberOfQuestions')  # Field name made lowercase.
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
        db_table = 'examinationcategories'
        unique_together = (('examinationid', 'category', 'company', 'deleted'),)


class Examinationexaminationvenues(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationid = models.BigIntegerField(db_column='ExaminationID')  # Field name made lowercase.
    venue = models.CharField(db_column='Venue', max_length=255)  # Field name made lowercase.
    firstbatchstarttime = models.DateTimeField(db_column='FirstBatchStartTime')  # Field name made lowercase.
    lastbatchendtime = models.DateTimeField(db_column='LastBatchEndTime')  # Field name made lowercase.
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
        db_table = 'examinationexaminationvenues'


class Examinationquestionoptions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationquestionid = models.BigIntegerField(db_column='ExaminationQuestionID')  # Field name made lowercase.
    optionhtml = models.TextField(db_column='OptionHtml')  # Field name made lowercase.
    answer = models.IntegerField(db_column='Answer')  # Field name made lowercase.
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
        db_table = 'examinationquestionoptions'


class Examinationquestions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationid = models.BigIntegerField(db_column='ExaminationID')  # Field name made lowercase.
    questionnumber = models.IntegerField(db_column='QuestionNumber')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    questionhtml = models.TextField(db_column='QuestionHtml')  # Field name made lowercase.
    marks = models.IntegerField(db_column='Marks')  # Field name made lowercase.
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
        db_table = 'examinationquestions'


class Examinations(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255)  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=255)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    showscorewhenfinished = models.IntegerField(db_column='ShowScoreWhenFinished')  # Field name made lowercase.
    numberofquestions = models.IntegerField(db_column='NumberOfQuestions')  # Field name made lowercase.
    questionselectionmode = models.CharField(db_column='QuestionSelectionMode', max_length=255)  # Field name made lowercase.
    questionspercategory = models.IntegerField(db_column='QuestionsPerCategory')  # Field name made lowercase.
    instructions = models.TextField(db_column='Instructions')  # Field name made lowercase.
    randomiseoptions = models.IntegerField(db_column='RandomiseOptions')  # Field name made lowercase.
    timedquestions = models.IntegerField(db_column='TimedQuestions')  # Field name made lowercase.
    useonlygracelakecbtbrowser = models.IntegerField(db_column='UseOnlyGraceLakeCBTBrowser')  # Field name made lowercase.
    useonlypremiercbtbrowser = models.IntegerField(db_column='UseOnlyPremierCBTBrowser')  # Field name made lowercase.
    physicaltest = models.IntegerField(db_column='PhysicalTest')  # Field name made lowercase.
    practiceexam = models.IntegerField(db_column='PracticeExam')  # Field name made lowercase.
    exampaused = models.IntegerField(db_column='ExamPaused')  # Field name made lowercase.
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
        db_table = 'examinations'
        unique_together = (('subject', 'company', 'deleted'),)


class Examinationschedulecapturedimages(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationscheduleid = models.BigIntegerField(db_column='ExaminationScheduleID')  # Field name made lowercase.
    machinename = models.TextField(db_column='MachineName')  # Field name made lowercase.
    imageblob = models.TextField(db_column='ImageBlob')  # Field name made lowercase.
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
        db_table = 'examinationschedulecapturedimages'


class Examinationschedulecategories(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationsceduleid = models.BigIntegerField(db_column='ExaminationSceduleID')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
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
        db_table = 'examinationschedulecategories'
        unique_together = (('examinationsceduleid', 'category', 'company', 'deleted'),)


class Examinationschedulequestionoptions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationscheduleid = models.BigIntegerField(db_column='ExaminationScheduleID')  # Field name made lowercase.
    optionno = models.IntegerField(db_column='OptionNo')  # Field name made lowercase.
    examinationquestionid = models.BigIntegerField(db_column='ExaminationQuestionID')  # Field name made lowercase.
    examinationquestionoptionid = models.BigIntegerField(db_column='ExaminationQuestionOptionID')  # Field name made lowercase.
    selected = models.IntegerField(db_column='Selected')  # Field name made lowercase.
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
        db_table = 'examinationschedulequestionoptions'


class Examinationschedulequestions(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    examinationscheduleid = models.BigIntegerField(db_column='ExaminationScheduleID')  # Field name made lowercase.
    questionno = models.IntegerField(db_column='QuestionNo')  # Field name made lowercase.
    examinationquestionid = models.BigIntegerField(db_column='ExaminationQuestionID')  # Field name made lowercase.
    correct = models.IntegerField(db_column='Correct')  # Field name made lowercase.
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
        db_table = 'examinationschedulequestions'


class Examinationschedules(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    venueid = models.CharField(db_column='VenueID', max_length=255)  # Field name made lowercase.
    examinationid = models.BigIntegerField(db_column='ExaminationID')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime')  # Field name made lowercase.
    actualstartdatetime = models.DateTimeField(db_column='ActualStartDateTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.
    percentagescore = models.DecimalField(db_column='PercentageScore', max_digits=64, decimal_places=30)  # Field name made lowercase.
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
        db_table = 'examinationschedules'
        unique_together = (('refno', 'examinationid', 'company', 'deleted'),)


class Examinationsubjects(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subjectid = models.CharField(db_column='SubjectID', max_length=255)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255)  # Field name made lowercase.
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
        db_table = 'examinationsubjects'
        unique_together = (('subjectid', 'company', 'deleted'),)


class Examinationvenues(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    venueid = models.CharField(db_column='VenueID', max_length=255)  # Field name made lowercase.
    venuename = models.CharField(db_column='VenueName', max_length=255)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.
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
        db_table = 'examinationvenues'
        unique_together = (('venueid', 'company', 'deleted'),)


class Guarantortosign(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='guarantorid', max_length=100)  # Field name made lowercase.
    requestid = models.CharField(db_column='requestid', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='status', max_length=100)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='datecreated', default=timezone.now)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guarantortosign'
        unique_together = (('guarantorid', 'requestid'),)


class GuarantorLists(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='drivername', max_length=255)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False


class Guarantordetails(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255)  # Field name made lowercase.
    localgovernmentarea = models.CharField(db_column='LocalGovernmentArea', max_length=255)  # Field name made lowercase.
    lcda = models.CharField(db_column='LCDA', max_length=255)  # Field name made lowercase.
    scheduled = models.IntegerField(db_column='Scheduled')  # Field name made lowercase.
    submittedforapproval = models.IntegerField(db_column='SubmittedForApproval')  # Field name made lowercase.
    placeofwork = models.CharField(db_column='PlaceofWork', max_length=255)  # Field name made lowercase.
    officeaddress = models.CharField(db_column='OfficeAddress', max_length=255)  # Field name made lowercase.
    positionheld = models.CharField(db_column='PositionHeld', max_length=255)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255)  # Field name made lowercase.
    remarkreason = models.CharField(db_column='RemarkReason', max_length=255)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=255)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    bvn = models.CharField(db_column='BVN', max_length=255)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=255)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='ModifiedDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recordversion = models.BigIntegerField(db_column='RecordVersion')  # Field name made lowercase.
    deleted = models.BigIntegerField(db_column='Deleted')  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guarantordetails'
        unique_together = (('guarantorid', 'company', 'deleted'), ('drn', 'phone', 'company', 'deleted'),)


class Guarantordocuments(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    guarantorid = models.BigIntegerField(db_column='GuarantorID')  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=255)  # Field name made lowercase.
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
        db_table = 'guarantordocuments'
        unique_together = (('guarantorid', 'documenttype', 'company', 'deleted'),)


class Guarantordocumenttypes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    guarantordocumenttype = models.CharField(db_column='GuarantorDocumentType', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    documentstatus = models.CharField(db_column='DocumentStatus', max_length=255)  # Field name made lowercase.
    ispassport = models.IntegerField(db_column='IsPassport')  # Field name made lowercase.
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
        db_table = 'guarantordocumenttypes'
        unique_together = (('guarantordocumenttype', 'company', 'deleted'),)


class Guarantorverificationitem(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    applicablecategory = models.CharField(db_column='ApplicableCategory', max_length=255)  # Field name made lowercase.
    requiregpscoordinate = models.IntegerField(db_column='RequireGPSCoordinate')  # Field name made lowercase.
    requireimage = models.IntegerField(db_column='RequireImage')  # Field name made lowercase.
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
        db_table = 'guarantorverificationitem'
        unique_together = (('itemid', 'company', 'deleted'),)


class Lcda(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lcdaid = models.CharField(db_column='LCDAId', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='ModifiedDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recordversion = models.BigIntegerField(db_column='RecordVersion')  # Field name made lowercase.
    deleted = models.BigIntegerField(db_column='Deleted')  # Field name made lowercase.
    lga = models.CharField(db_column='LGA', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lcda'
        unique_together = (('lga', 'lcdaid', 'company', 'deleted'),)


class Localgovernments(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stateid = models.CharField(db_column='StateID', max_length=255)  # Field name made lowercase.
    localgovtid = models.CharField(db_column='LocalGovtID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
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
        db_table = 'localgovernments'
        unique_together = (('stateid', 'localgovtid', 'deleted'),)


class States(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stateid = models.CharField(db_column='StateID', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
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
        db_table = 'states'
        unique_together = (('name', 'deleted'), ('stateid', 'deleted'),)


class Tempdispatchschedule(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dispatchid = models.CharField(db_column='DispatchID', max_length=255)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    dispatchoperationalarea = models.CharField(db_column='DispatchOperationalArea', max_length=255)  # Field name made lowercase.
    verificationlocation = models.CharField(db_column='VerificationLocation', max_length=255)  # Field name made lowercase.
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
        db_table = 'tempdispatchschedule'
        unique_together = (('drn', 'guarantorid', 'date', 'createdby', 'company', 'deleted'),)


class Test(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    testid = models.CharField(db_column='TestId', max_length=255)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
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
        db_table = 'test'
        unique_together = (('testid', 'company', 'deleted'),)


class Testquestion(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    testquestionid = models.CharField(db_column='TestQuestionId', max_length=255)  # Field name made lowercase.
    questions = models.TextField(db_column='Questions')  # Field name made lowercase.
    testid = models.CharField(db_column='TestId', max_length=255)  # Field name made lowercase.
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
        db_table = 'testquestion'
        unique_together = (('testquestionid', 'company', 'deleted'),)


class Testresult(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    testscheduleid = models.BigIntegerField(db_column='TestScheduleId')  # Field name made lowercase.
    testquestionid = models.BigIntegerField(db_column='TestQuestionId')  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=255)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255)  # Field name made lowercase.
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
        db_table = 'testresult'
        unique_together = (('testscheduleid', 'testquestionid', 'company', 'deleted'),)


class Testschedule(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scheduleid = models.CharField(db_column='ScheduleId', max_length=255)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    testid = models.CharField(db_column='TestId', max_length=255)  # Field name made lowercase.
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
        db_table = 'testschedule'
        unique_together = (('scheduleid', 'company', 'deleted'),)


class Verificationitem(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemid = models.CharField(db_column='ItemID', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    applicablecategory = models.CharField(db_column='ApplicableCategory', max_length=255)  # Field name made lowercase.
    requiregpscoordinate = models.IntegerField(db_column='RequireGPSCoordinate')  # Field name made lowercase.
    requireimage = models.IntegerField(db_column='RequireImage')  # Field name made lowercase.
    requirenote = models.IntegerField(db_column='RequireNote')  # Field name made lowercase.
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
        db_table = 'verificationitem'
        unique_together = (('itemid', 'company', 'deleted'),)


class Verificationparameters(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maxscheduleperdispatch = models.IntegerField(db_column='MaxSchedulePerDispatch')  # Field name made lowercase.
    dispatchschedulemode = models.CharField(db_column='DispatchScheduleMode', max_length=255)  # Field name made lowercase.
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
        db_table = 'verificationparameters'


class Verificationresult(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    verificationitem = models.CharField(db_column='VerificationItem', max_length=255)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=255)  # Field name made lowercase.
    note = models.TextField(db_column='Note')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    statusreason = models.CharField(db_column='StatusReason', max_length=255)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='ModifiedDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recordversion = models.BigIntegerField(db_column='RecordVersion')  # Field name made lowercase.
    deleted = models.BigIntegerField(db_column='Deleted')  # Field name made lowercase.
    dispatchscheduleid = models.BigIntegerField(db_column='DispatchScheduleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'verificationresult'
        unique_together = (('dispatchscheduleid', 'refno', 'verificationitem', 'company', 'deleted'),)


class Verificationresultimages(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    verificatioresultid = models.BigIntegerField(db_column='VerificatioResultID')  # Field name made lowercase.
    imagedata = models.TextField(db_column='ImageData')  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=255)  # Field name made lowercase.
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
        db_table = 'verificationresultimages'


class Verificationresultsapproval(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drn = models.CharField(db_column='DRN', max_length=255)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GuarantorID', max_length=255)  # Field name made lowercase.
    verificationitem = models.CharField(db_column='VerificationItem', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.
    firstapproval = models.IntegerField(db_column='FirstApproval')  # Field name made lowercase.
    secondapproval = models.IntegerField(db_column='SecondApproval')  # Field name made lowercase.
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
        db_table = 'verificationresultsapproval'
        unique_together = (('drn', 'verificationitem', 'category', 'guarantorid', 'company', 'deleted'),)


class Verifiedbankaccounts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=255)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=255)  # Field name made lowercase.
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
        db_table = 'verifiedbankaccounts'
        unique_together = (('bank', 'accountnumber', 'company', 'deleted'),)


class Verifiedbvns(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bvn = models.CharField(db_column='BVN', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=255)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateofBirth')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255)  # Field name made lowercase.
    registrationdate = models.DateField(db_column='RegistrationDate')  # Field name made lowercase.
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
        db_table = 'verifiedbvns'
        unique_together = (('bvn', 'company', 'deleted'),)
