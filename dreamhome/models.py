# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Privateowner(models.Model):
    ownerno = models.CharField(db_column='OwnerNo', primary_key=True, max_length=6)  # Field name made lowercase.
    ownername = models.CharField(db_column='ownerName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='homeAddress', unique=True, max_length=100)  # Field name made lowercase.
    telno = models.CharField(db_column='telNo', max_length=15)  # Field name made lowercase.
    regbranch = models.ForeignKey('Branch', models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    typeofbusiness = models.CharField(db_column='typeOfBusiness', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='contactName', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrivateOwner'


class Propertyforrent(models.Model):
    propertyno = models.CharField(db_column='propertyNo', primary_key=True, max_length=6)  # Field name made lowercase.
    proptype = models.CharField(db_column='propType', max_length=10)  # Field name made lowercase.
    rooms = models.SmallIntegerField()
    rent = models.IntegerField()
    address = models.CharField(unique=True, max_length=100)
    regowner = models.ForeignKey(Privateowner, models.DO_NOTHING, db_column='regOwner')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.
    regbranch = models.ForeignKey('Branch', models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PropertyForRent'


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
    preftype = models.CharField(db_column='prefType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maxrent = models.IntegerField(db_column='maxRent')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


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
    proptype = models.CharField(db_column='propType', max_length=10)  # Field name made lowercase.
    rooms = models.SmallIntegerField()
    rent = models.IntegerField()
    address = models.CharField(unique=True, max_length=100)
    regowner = models.ForeignKey(Privateowner, models.DO_NOTHING, db_column='regOwner')  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff')  # Field name made lowercase.
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch')  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.

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

    class Meta:
        managed = False
        db_table = 'view_report'
