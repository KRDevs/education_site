from django.contrib import admin

from subject.models import Lecture, Test, TestOption, Practice, Laboratory, Videos

admin.site.register(Lecture)
admin.site.register(Practice)
admin.site.register(Laboratory)
admin.site.register(Test)
admin.site.register(TestOption)
admin.site.register(Videos)
