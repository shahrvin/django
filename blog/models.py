from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os 
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg','.png' , '.webp']
    if not ext.lower() in valid_extensions :
        raise ValidationError("file extension not supported")



class UserProfile(models.Model):
    user = models.OneToOneField(User ,  on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null= True , blank=True , validators=[validate_file_extension])
    description = models.TextField(max_length=512 , null = False , blank= False)
    def __str__(self):
        return self.user.first_name +" " + self.user.last_name

class Article(models.Model):
    title = models.CharField(max_length=312 , null= False , blank= False)
    cover = models.FileField(upload_to='files/article_cover/',null = False , blank= False , validators=[validate_file_extension])
    created = models.DateTimeField()
    content = RichTextField(default=datetime.now , blank = False)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category (models.Model):
    title = models.CharField(max_length=200 , null = False , blank = False)
    cover = models.FileField(upload_to='files/category_cover' , null = False , blank = False , validators=[validate_file_extension])

    def __str__(self):
        return self.title
    