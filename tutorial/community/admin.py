from django.contrib import admin

# Register your models here.

from .models import Student, Assignment,Team,Tutor,Unit_Coordinator,Project_Supervisor
# Register your models here.


admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Team)
admin.site.register(Tutor)
admin.site.register(Unit_Coordinator)
admin.site.register(Project_Supervisor)
