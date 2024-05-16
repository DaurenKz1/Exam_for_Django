# Generated by Django 5.0.6 on 2024-05-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_taskDetails',
            fields=[
                ('taskId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('deadlineDate', models.CharField(max_length=50)),
                ('deadlineTime', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('filename', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Todo_userDetails',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('mobileNumber', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=30)),
                ('profilePic', models.ImageField(default='/images/user.png', upload_to='media/')),
                ('bio', models.CharField(default='Hey there! I am using TaskMate.', max_length=500)),
            ],
        ),
    ]