from django.contrib import admin
from .models import Question, Choice, Customer

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'date_time', 'delete')
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date information', {'fields': ['date_time']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['date_time']
    search_fields = ['id']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Customer,CustomerAdmin)

