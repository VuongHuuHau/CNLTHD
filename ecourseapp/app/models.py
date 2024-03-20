from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    update_date = models.DateTimeField(auto_now=True,null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
class Category(models.Model):
    name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

class course(BaseModel):
    subject = models.CharField(max_length=250,null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='app/%Y/%m')
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    tag=models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('category','subject')

class Lesson(BaseModel):
    subject = models.CharField(max_length=250,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to='lesson/%Y/%m')
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')

    class Meta:
     unique_together = ('course','subject')

class Tag(BaseModel):
    name = models.CharField(max_length=50 , unique=True)