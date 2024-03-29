# Generated by Django 3.1.7 on 2021-07-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sac_app', '0002_auto_20210716_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='act_id',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='activities',
            name='act_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='activities',
            name='act_organizer_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='activities',
            name='act_organizer_phone',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='activities',
            name='org_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='activities_modified',
            name='act_id',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='activities_modified',
            name='act_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='activities_modified',
            name='act_organizer_name',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='activities_modified',
            name='act_organizer_phone',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='bbs_comments',
            name='bbs_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='managers',
            name='man_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='managers',
            name='man_password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='org_directmessages',
            name='accept_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='org_directmessages',
            name='send_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='organizers',
            name='org_header_college',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='organizers',
            name='org_header_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='organizers',
            name='org_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='organizers',
            name='org_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='organizers_modified',
            name='org_header_college',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='organizers_modified',
            name='org_header_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='organizers_modified',
            name='org_header_phone',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='organizers_modified',
            name='org_id',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='organizers_modified',
            name='org_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='stu_directmessages',
            name='accept_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='stu_directmessages',
            name='send_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_Email',
            field=models.EmailField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_college',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_gender',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_id',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_major',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_password',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='students',
            name='stu_phone',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_header_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_header_phone',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_introduction',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
