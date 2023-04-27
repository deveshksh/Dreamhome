# Generated by Django 4.2 on 2023-04-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('telno', models.CharField(blank=True, db_column='telNo', max_length=20, null=True)),
            ],
            options={
                'db_table': 'branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientno', models.CharField(db_column='clientNo', max_length=5, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=30, null=True)),
                ('lname', models.CharField(blank=True, max_length=30, null=True)),
                ('preftype', models.CharField(blank=True, db_column='prefType', max_length=10, null=True)),
                ('maxrent', models.IntegerField(blank=True, db_column='maxRent', null=True)),
                ('regdate', models.DateField(blank=True, db_column='regDate', null=True)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Privateowner',
            fields=[
                ('ownerno', models.CharField(db_column='OwnerNo', max_length=5, primary_key=True, serialize=False)),
                ('ownername', models.CharField(blank=True, db_column='ownerName', max_length=30, null=True)),
                ('homeaddress', models.CharField(blank=True, db_column='homeAddress', max_length=100, null=True)),
                ('telno', models.CharField(blank=True, db_column='telNo', max_length=15, null=True)),
                ('regdate', models.DateField(blank=True, db_column='regDate', null=True)),
                ('typeofbusiness', models.CharField(blank=True, db_column='typeOfBusiness', max_length=20, null=True)),
                ('contactname', models.CharField(blank=True, db_column='contactName', max_length=40, null=True)),
            ],
            options={
                'db_table': 'privateowner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Propertyforrent',
            fields=[
                ('propertyno', models.CharField(db_column='propertyNo', max_length=5, primary_key=True, serialize=False)),
                ('proptype', models.CharField(blank=True, db_column='propType', max_length=10, null=True)),
                ('rooms', models.SmallIntegerField(blank=True, null=True)),
                ('rent', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('regdate', models.DateField(blank=True, db_column='regDate', null=True)),
            ],
            options={
                'db_table': 'propertyforrent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=15, null=True)),
                ('lname', models.CharField(blank=True, max_length=15, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('pos', models.CharField(blank=True, max_length=20, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('supervisor_no', models.CharField(blank=True, max_length=5, null=True)),
                ('manager_date', models.DateField(blank=True, null=True)),
                ('manager_bonus', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
    ]