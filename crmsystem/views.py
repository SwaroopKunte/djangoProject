from rest_framework_mongoengine import viewsets as meviewsets
from crmsystem.models import Employee
from crmsystem.serializers import EmployeeSerializer

class EmployeesView(meviewsets.ModelViewSet):
    lookup_field = 'EmpId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer