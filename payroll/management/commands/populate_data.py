from django.core.management.base import BaseCommand
from payroll.models import Employee, Attendance

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        # Add Employees
        employees = [
            {'emp_no': 1, 'basic_pay': 10000, 'it_percent': 15},
            {'emp_no': 2, 'basic_pay': 15000, 'it_percent': 20},
            {'emp_no': 3, 'basic_pay': 20000, 'it_percent': 25},
        ]

        for emp in employees:
            Employee.objects.create(emp_no=emp['emp_no'], basic_pay=emp['basic_pay'], it_percent=emp['it_percent'])

        # Add Attendance Records
        attendances = [
            {'emp_no': 1, 'month': 'April', 'days_present': 25},
            {'emp_no': 1, 'month': 'May', 'days_present': 23},
            {'emp_no': 1, 'month': 'June', 'days_present': 21},
            {'emp_no': 2, 'month': 'April', 'days_present': 25},
            {'emp_no': 2, 'month': 'May', 'days_present': 23},
            {'emp_no': 2, 'month': 'June', 'days_present': 21},
            {'emp_no': 3, 'month': 'April', 'days_present': 25},
            {'emp_no': 3, 'month': 'May', 'days_present': 23},
            {'emp_no': 3, 'month': 'June', 'days_present': 21},
        ]

        for att in attendances:
            emp = Employee.objects.get(emp_no=att['emp_no'])
            Attendance.objects.create(emp_no=emp, month=att['month'], days_present=att['days_present'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with initial data'))
