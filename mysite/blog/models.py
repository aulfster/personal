from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Post(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    post_text = models.TextField(default = "Don't leave blank")
    post_summary = models.TextField(default = "Don't leave blank")
    publication_date = models.DateField()
    photo = models.ImageField(upload_to='blogPhotos', null = True)

    def __unicode__(self):
        return self.title
