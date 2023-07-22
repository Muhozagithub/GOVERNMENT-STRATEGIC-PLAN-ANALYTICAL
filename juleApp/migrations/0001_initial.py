# Generated by Django 2.0 on 2023-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='roadissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('datedata', models.CharField(max_length=100)),
                ('NID', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('Gendar', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('cells', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('Issuedetails', models.CharField(max_length=100)),
                ('Leadervillage', models.CharField(max_length=100)),
                ('leadercell', models.CharField(max_length=100)),
                ('leadersector', models.CharField(max_length=100)),
                ('leaderdidtrict', models.CharField(max_length=100)),
                ('mainroad', models.CharField(max_length=100)),
                ('lenght', models.CharField(max_length=100)),
                ('relateddata', models.CharField(max_length=100)),
                ('vlagename', models.CharField(max_length=100)),
                ('cellname', models.CharField(max_length=100)),
                ('secotname', models.CharField(max_length=100)),
                ('phonecvilage', models.CharField(max_length=100)),
                ('phoneCells', models.CharField(max_length=100)),
                ('phoneSector', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('repeatPassword', models.CharField(max_length=100)),
            ],
        ),
    ]
