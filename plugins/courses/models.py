from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagging.fields import TagField

from perms.models import TendenciBaseModel
from courses.managers import CourseManager

class Course(TendenciBaseModel):
    """
    Courses plugin base model.
    You can think of this as test since there will be several questions
    linked to it.
    """
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'))
    retries = models.IntegerField(_(u'Retries'), help_text=u'Number of retries allowed (0, means unlimited)', default=0)
    retry_interval = models.IntegerField(_(u'Retry Interval'), help_text=u'Number of hours before another retry', default=0)
    passing_score = models.DecimalField(_(u'Passing Score'), help_text=u'out of 100%', max_digits=5, decimal_places=2)
    deadline = models.DateTimeField(_(u'Deadline'), default=datetime(datetime.now().year+1, datetime.now().month, datetime.now().day))
    close_after_deadline = models.BooleanField(_(u'Close After Deadline'), default=False)
    tags = TagField(blank=True, help_text='Tag 1, Tag 2, ...')
    
    objects = CourseManager()
    
    class Meta:
        permissions = (("view_course","Can view course"),)
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ("courses.detail", [self.pk])
    
    @property
    def total_points(self):
        total_points = 0
        for question in self.questions.all():
            total_points = total_points + question.point_value
        return total_points


class Question(models.Model):
    """
    Represents a single question for a course.
    point_value should always be equal to 100 over total number of course questions.
    """
    course = models.ForeignKey(Course, related_name="questions")
    question = models.CharField(_(u'Question'), max_length=200)
    answer_choices = models.CharField(_(u'Answer Choices'), help_text=_(u'separated by comma'), max_length=200)
    answer = models.CharField(_(u'Correct Answer'), max_length=200)
    point_value = models.IntegerField(_(u'Point Value'), default=0)
    
    def __unicode__(self):
        return "%s: %s" % (self.course.title, self.question)


class CourseAttempt(models.Model):
    """
    Represents course attempts.
    We can also use this to represent course completions and failures.
    """
    course = models.ForeignKey(Course, related_name="attempts")
    user = models.ForeignKey(User)
    score =  models.DecimalField(_(u'Score'), help_text=_(u'out of 100%'), max_digits=5, decimal_places=2)
    create_dt = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(_(u'Notes'), blank=True, default=u'')
    
    def __unicode__(self):
        return "%s" % (self.course.title)
    
    @property
    def passed(self):
        if self.score >= self.course.passing_score:
            return True
        return False
