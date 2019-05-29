from django.db import models
# from enum import Enum
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    notes = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.name

# class UserType(ENUM):
#     1 = 'Teacher'
#     2 = 'Student'
#     3 = 'Subscriber'


class UserProfileInfo(models.Model):
    MAYBECHOICE = (
        ('1', 'Teacher'),
        ('2', 'Student'),
        ('3', 'Subscriber'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    user_type = models.CharField(max_length=1, choices=MAYBECHOICE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Class(models.Model):
    class_name = models.CharField(max_length=255)
    class_day = models.CharField(max_length=255)
    class_time = models.CharField(max_length=255)
    class_type = models.CharField(max_length=1, choices=(
        ('1', 'Primary'),
        ('2', 'Secondary'),
        ('3', 'Higher'),
        ('4', 'Graduation'),
    ))
    class_status = models.CharField(max_length=1, choices=(('1', 'Active'), ('0', 'Inactive'),))

    def __str__(self):
        return self.class_name


class Subject(models.Model):
    subject_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=255, blank=True)
    subject_status = models.CharField(max_length=1, choices=(('1', 'Active'), ('0', 'Inactive'),))

    def __str__(self):
        return self.subject_name


class Question(models.Model):
    # models.ManyToManyField(Test)
    ques_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ques_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    ques_text = models.TextField()
    ques_marks = models.CharField(max_length=255)
    ques_type = models.CharField(max_length=1, choices=(('1', 'Objective'), ('2', 'Subjective'),))
    ques_note = models.TextField(blank=True)

    def __str__(self):
        return self.ques_text + '==(' + self.ques_subject.subject_name + '/' + self.ques_class.class_name +\
               '/[' + self.ques_marks + '])'


class Test(models.Model):
    test_question = models.ManyToManyField(Question, blank=True)
    test_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    test_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_topic = models.CharField(max_length=255)
    test_marks = models.CharField(max_length=255)
    test_note = models.TextField()
    test_status = models.CharField(max_length=1, choices=(('1', 'Active'), ('0', 'Inactive'),))
    test_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.test_subject.subject_name


class TestResult(models.Model):
    result_user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result_marks = models.CharField(max_length=255)
    result_grade = models.CharField(max_length=255)
    result_percentage = models.CharField(max_length=255)
    result_suggestion = models.CharField(max_length=255)
    result_status = models.CharField(max_length=1, choices=(('1', 'Active'), ('0', 'Inactive'),))
    test_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.result_user.username