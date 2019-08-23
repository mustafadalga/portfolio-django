from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')



    def __str__(self):
        return self.title

#create a blog models
# add the blog app to the settings
#create a migration
#migrate
#add to the admin

a="selam"

