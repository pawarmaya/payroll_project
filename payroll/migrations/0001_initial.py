# Generated by Django 4.2.13 on 2024-06-08 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('basic_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('it_percent', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('days_present', models.IntegerField()),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
        ),
    ]
