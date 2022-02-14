
from django.contrib import admin

from Token_App.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','salary','address']
    search_fields = ['ename']
    list_editable = ['salary']
    list_display_links = ["eno"]
    list_filter = ['ename']
    # list_per_page = 2
    # readonly_fields = ['eno']
    # fields = ['eno','ename','salary']
    exclude = ['address']



admin.site.register(Employee,EmployeeAdmin)