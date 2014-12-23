from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    '''
    An abstract base class model that provides selfupdating
    created and modified fields.
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SlugManager(models.Manager):
    def filter_slug(self, *args):
        return self.filter(slug=args[0])


class SaveSlug(models.Model):
    '''
    Base class to create a slugfield
    '''
    title = models.CharField(max_length=40)
    slug = models.SlugField(db_index=True, unique=True, 
        editable=False, blank=True) 

    objects = SlugManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.title)
        
        super(SaveSlug, self).save(*args, **kwargs)  


class User(AbstractUser):
    '''
    Extended User class. Set this up in the beginning unless you are
    absolutely sure the User class will not expand.
    '''
    alive = models.BooleanField(default=True)

    