from django.contrib import admin
from .models import Question
from .models import FillInBlank
from .models import Question_by_topic
from .models import FillInBlank_by_topic
# Register your models here.

admin.site.register(Question)
admin.site.register(FillInBlank)
admin.site.register(Question_by_topic)
admin.site.register(FillInBlank_by_topic)

