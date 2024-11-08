from django.db import models
from main.models import Student, Instructor, Course

STATUS = ((1, "Published"),(0, "Archived"),(2,"Mark as Offensive"))

class StudentDiscussion(models.Model):
    content = models.TextField(max_length=1600, null=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='discussions')
    sent_by = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='discussions')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return self.content[:30]

    def time(self):
        return self.sent_at.strftime("%d-%b-%y, %I:%M %p")


class InstructorDiscussion(models.Model):
    content = models.TextField(max_length=1600, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courseDiscussions')
    sent_by = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courseDiscussions')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return self.content[:30]

    def time(self):
        return self.sent_at.strftime("%d-%b-%y, %I:%M %p")