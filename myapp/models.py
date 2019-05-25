from django.db import models as md
from django.conf import settings

from django.utils import timezone
# Create your models here.
from accounts.models import User_info

class Title_info(md.Model):
	Title_name=md.CharField(max_length=50)
	Title_ISBN=md.CharField(max_length=30,unique=True)

	def __str__(self):
		return self.Title_name

class Book_info(md.Model):
	Book_ISBN=md.ForeignKey(Title_info,on_delete=md.CASCADE)

	def __str__(self):
		return self.Book_ISBN.Title_name

class Lend_info(md.Model):
	Lend_date=md.DateTimeField(default=timezone.now)
	Lend_book=md.ForeignKey(Book_info,on_delete=md.CASCADE)
	Lend_user=md.ForeignKey(User_info,on_delete=md.CASCADE)

class Review_info(md.Model):
	SCORE_CHOICES=(
		(1,"おすすめしない"),
		(2,"あまりおすすめしない"),
		(3,"どちらでもない"),
		(4,"おすすめする"),
		(5,"強くおすすめする"),
	)
	Review_title=md.ForeignKey(Title_info,on_delete=md.CASCADE)
	Review_score=md.PositiveIntegerField(choices=SCORE_CHOICES)

class Return_info(md.Model):
	Return_lend=md.OneToOneField(Lend_info,on_delete=md.CASCADE)
	Return_date=md.DateTimeField(default=timezone.now)




