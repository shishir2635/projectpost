# Generated by Django 2.0.1 on 2018-02-02 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the person', max_length=100)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science And Engineering'), ('IT', 'Information Technology'), ('EC', 'Electronics Engineering'), ('EEE', 'Electrical And Electronics Engineering'), ('CE', 'Civil Engineering'), ('ME', 'Mechanical Engineering'), ('EE', 'Electrical Engineering'), ('IC', 'Instrumentation and Control')], help_text="Enter Person's Branch Here", max_length=100)),
                ('year', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], help_text='Enter the year of study of person', max_length=10)),
                ('num_posts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=450)),
                ('dat', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='names.names')),
            ],
        ),
    ]