from django.contrib import admin
from .models import Contact, UserProfileInfo, Subject, Class, Test, Question, TestResult
from django.utils.html import format_html

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_class')
    list_filter = ('subject_name', 'subject_class')
    list_per_page = 5
    fields = ['subject_class', ('subject_name', 'subject_type'), 'subject_status']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject')
    list_per_page = 5
    fields = [('name', 'email'), 'subject', 'notes']


class UserProfileInfoAdmin(admin.ModelAdmin):
    # list_display = ('profile_pic',)
    list_per_page = 5

    def image_tag(self, obj):
        return format_html('<img src="{}" style="height:50px;width:50px;border-radius: 50%;" />'.format(obj.profile_pic.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'name', 'email', 'user_type']

    def name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def email(self, obj):
        return obj.user.email

    list_filter = ('user_type',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'class_day', 'class_time', 'class_type')
    list_filter = ('class_name', 'class_day', 'class_time', 'class_type')
    list_per_page = 5
    fields = ['class_name', ('class_day', 'class_time'), ('class_type', 'class_status')]


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_topic', 'test_class', 'test_subject', 'test_marks', 'test_note', 'test_date', 'get_quetions',)
    list_filter = ('test_topic', 'test_class', 'test_subject', 'test_marks', 'test_note', 'test_date')
    list_per_page = 5
    fields = [
        ('test_class', 'test_subject'),
        ('test_topic', 'test_marks'),
        'test_note',
        ('test_status', 'test_date', 'test_question')]
    filter_horizontal = ('test_question',)

    def get_quetions(self, obj):
        return "\n".join([p.questions for p in obj.test_question.all()])


class TestResultAdmin(admin.ModelAdmin):
    list_display = ('result_user',
                    'result_test',
                    'test_date',
                    'result_marks',
                    'result_grade',
                    'result_percentage',
                    'result_suggestion')
    list_filter = ('result_user',
                   'result_test',
                   'test_date',
                   'result_marks',
                   'result_grade',
                   'result_percentage',
                   'result_suggestion')
    list_per_page = 5


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('ques_class', 'ques_subject', 'ques_text', 'ques_marks', 'ques_type', 'ques_note')
    list_filter = ('ques_class', 'ques_subject', 'ques_text', 'ques_marks', 'ques_type', 'ques_note')
    list_per_page = 5

# myModels = [Contact, Subject, UserProfileInfo, Class, Test, TestResult, Question]  # iterable list


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.site_header = 'Star Study'



