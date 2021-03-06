# Generated by Django 2.2.5 on 2020-03-04 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=10)),
                ('phone', models.PositiveIntegerField(max_length=10)),
                ('room', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Hostel')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Problem')),
            ],
        ),
    ]
