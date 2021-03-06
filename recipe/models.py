# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse
from .fields import ThumbnailImageField
from django.contrib.auth.models import User
from django.utils.text import slugify
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
@python_2_unicode_compatible
class Recipe(models.Model):
    title = models.CharField('레시피 설명',max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    foodname = models.CharField('음식 이름',max_length=25)
    titleimage = ThumbnailImageField('대표 사진',upload_to='Recipe/titleiamge/%y/%m/%d')
    servings = models.IntegerField('조리분량',default=1, help_text='인분')
    cookingtime = models.IntegerField('조리시간(분)',default=1, help_text='분')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    scraps = models.IntegerField(default=0)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
        db_table  = 'recipe_posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe:recipe_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Recipe, self).save(*args, **kwargs)

# When a user flexibly adds or deletes an ingredient field and a quantity field,
#the field of the model also needs to be changed accordingly. 
@python_2_unicode_compatible
class Foodinfo(models.Model):
    foodinfo = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField('재료정보',max_length=200,blank=True)
    quantity = models.CharField('재료량: 포기, 개, 공기',max_length=200,blank=True, help_text='재료량: 포기, 개, 공기')

    def __str__(self):
        return self.ingredient

# When a user flexibly adds or deletes an image field and a text field, 
#the field of the model also needs to be changed accordingly.        
@python_2_unicode_compatible
class Recipeinfo(models.Model):
    recipeinfo = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = ThumbnailImageField(upload_to='Recipe/content/%y/%m/%d')
    description = models.TextField('Recipe Description', blank=True)
   
    def __str__(self):
        return self.description

@python_2_unicode_compatible
class ReComment(models.Model):
    Recipecomment = models.ForeignKey(Recipe, null=True)
    slug = models.CharField('slug',max_length=100, default='')
    user = models.CharField('user',max_length=100, default='')
    comments = models.TextField('comments', null=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True, null=True)
    
    def __str__(self):
        return self.comments
   