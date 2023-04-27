# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Branch(models.Model):
    branch_no = models.CharField(primary_key=True, max_length=6)
    address = models.CharField(unique=True, max_length=100)
    telno = models.CharField(db_column='telNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'
    
    def __str__(self):
        return f"{self.branch_no}"


class Client(models.Model):
    clientno = models.CharField(db_column='clientNo', primary_key=True, max_length=6)  # Field name made lowercase.
    fname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch', blank=True, null=True)  # Field name made lowercase.
    preftype = models.CharField(db_column='prefType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maxrent = models.IntegerField(db_column='maxRent', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Privateowner(models.Model):
    ownerno = models.CharField(db_column='ownerNo', primary_key=True, max_length=6)  # Field name made lowercase.
    ownername = models.CharField(db_column='ownerName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='homeAddress', unique=True, max_length=100)  # Field name made lowercase.
    telno = models.CharField(db_column='telNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch', blank=True, null=True)  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    typeofbusiness = models.CharField(db_column='typeOfBusiness', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='contactName', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'privateowner'
    def __str__(self):
        return f"{self.ownerno} {self.ownername}"


class Propertyforrent(models.Model):
    propertyno = models.CharField(db_column='propertyNo', primary_key=True, max_length=6)  # Field name made lowercase.
    proptype = models.CharField(db_column='propType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rooms = models.SmallIntegerField(blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    address = models.CharField(unique=True, max_length=100)
    regowner = models.ForeignKey(Privateowner, models.DO_NOTHING, db_column='regOwner', blank=True, null=True)  # Field name made lowercase.
    regstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='regStaff', blank=True, null=True)  # Field name made lowercase.
    regbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='regBranch', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyforrent'
        
    def __str__(self):
        return f"{self.propertyno} {self.address}"


class Staff(models.Model):
    staff_no = models.CharField(primary_key=True, max_length=6)
    fname = models.CharField(max_length=15, blank=True, null=True)
    lname = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    branch_no = models.ForeignKey(Branch, models.DO_NOTHING, db_column='branch_no', blank=True, null=True)
    pos = models.CharField(max_length=20, blank=True, null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    supervisor_no = models.CharField(max_length=5, blank=True, null=True)
    manager_date = models.DateField(blank=True, null=True)
    manager_bonus = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

    def __str__(self):
        return f"{self.staff_no}"