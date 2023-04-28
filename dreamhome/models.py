# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branch(models.Model):
    branch_no = models.CharField(primary_key=True, max_length=6)
    address = models.CharField(unique=True, max_length=100)
    telno = models.CharField(db_column='telNo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class Client(models.Model):
    clientno = models.CharField(db_column='clientNo', primary_key=True, max_length=6)  # Field name made lowercase.
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    preftype = models.ForeignKey('Preferences', models.DO_NOTHING, db_column='prefType', blank=True, null=True)  # Field name made lowercase.
    maxrent = models.IntegerField(db_column='maxRent')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Preferences(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'preferences'


class Privateowner(models.Model):
    ownerno = models.CharField(db_column='ownerNo', primary_key=True, max_length=6)  # Field name made lowercase.
    ownername = models.CharField(db_column='ownerName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='homeAddress', unique=True, max_length=100)  # Field name made lowercase.
    telno = models.CharField(db_column='telNo', max_length=15)  # Field name made lowercase.
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    typeofbusiness = models.CharField(db_column='typeOfBusiness', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='contactName', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'privateowner'


class Propertyforrent(models.Model):
    propertyno = models.CharField(db_column='propertyNo', primary_key=True, max_length=6)  # Field name made lowercase.
    proptype = models.ForeignKey(Preferences, models.DO_NOTHING, db_column='propType')  # Field name made lowercase.
    rooms = models.SmallIntegerField()
    rent = models.IntegerField()
    address = models.CharField(unique=True, max_length=100)
    regowner = models.ForeignKey(Privateowner, models.DO_NOTHING, db_column='regOwner')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    rent_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'propertyforrent'


class Staff(models.Model):
    staff_no = models.CharField(primary_key=True, max_length=6)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    sex = models.CharField(max_length=1)
    dob = models.DateField()
    branch_no = models.CharField(max_length=6)
    pos = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=6, decimal_places=0)
    supervisor_no = models.CharField(max_length=5, blank=True, null=True)
    manager_date = models.DateField(blank=True, null=True)
    manager_bonus = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class ViewReport(models.Model):
    propertyno = models.CharField(db_column='propertyNo', max_length=6)  # Field name made lowercase.
    clientno = models.ForeignKey(Client, models.DO_NOTHING, db_column='clientNo')  # Field name made lowercase.
    view_date = models.DateField()
    comment = models.CharField(max_length=256, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'view_report'

class Lease(models.Model):
    clientno = models.ForeignKey(Client, models.DO_NOTHING, db_column='clientno')
    propertyno = models.OneToOneField(Propertyforrent, models.DO_NOTHING, db_column='propertyno', primary_key=True)
    rent = models.IntegerField()
    payment_method = models.CharField(max_length=30)
    deposit_paid = models.IntegerField()
    rent_start = models.DateField()
    rent_finish = models.DateField(blank=True, null=True)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lease'
