from django.contrib import admin

# Register your models here.

from .models import Student, Poll, Choice, Assignment, Team
# Register your models here.

admin.site.register(Student)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Assignment)
admin.site.register(Team)
