from django.contrib import admin
from companies.models import Companies
from employee.models import Employee, Education, Jobs, Skills, Languages

admin.site.register(Companies)
admin.site.register(Employee)
admin.site.register(Education)
admin.site.register(Jobs)
admin.site.register(Skills)
admin.site.register(Languages)
