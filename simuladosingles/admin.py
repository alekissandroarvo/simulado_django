from django.contrib import admin
from .models import Question
from .models import FillInBlank
# Register your models here.

admin.site.register(Question)
admin.site.register(FillInBlank)
