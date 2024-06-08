from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Attendance
from decimal import Decimal
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO  # Import BytesIO

def payroll_dashboard(request):
    employees = Employee.objects.all()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    context = {'employees': employees, 'months': months}
    
    if request.method == "POST":
        emp_no = request.POST.get("emp_no")
        month = request.POST.get("month")
        download = request.POST.get("download")
        
        try:
            employee = Employee.objects.get(emp_no=emp_no)
            attendance = Attendance.objects.get(emp_no=employee, month=month)
            
            days_fraction = Decimal(attendance.days_present) / Decimal(30)
            gross_pay = employee.basic_pay * days_fraction
            net_pay = gross_pay - (gross_pay * (employee.it_percent / Decimal(100)))
            
            context.update({
                'gross_pay': gross_pay,
                'net_pay': net_pay,
                'selected_emp': employee,
                'selected_month': month,
                'attendance': attendance
            })
            
            if download == "yes":
                pdf = render_to_pdf('payroll/salary_slip.html', context)
                return HttpResponse(pdf, content_type='application/pdf')
            
        except (Employee.DoesNotExist, Attendance.DoesNotExist):
            context['error'] = "No attendance record found for the selected month or employee."
    
    return render(request, 'payroll/dashboard.html', context)

def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(template.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None
