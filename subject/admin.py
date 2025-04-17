from django.contrib import admin

from subject.models import Lecture, Test, TestOption, Practice, Laboratory

admin.site.register(Lecture)
admin.site.register(Practice)
admin.site.register(Laboratory)
admin.site.register(Test)
admin.site.register(TestOption)
