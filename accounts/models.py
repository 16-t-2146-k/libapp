from django.db import models as md
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_info(AbstractUser):
	# DEPT_CHOICES=(
	# 	(10,"工学部"),
	# 	(20,"教育学部"),
	# 	(99,"管理課")
	# )
	# Dept_code=md.PositiveIntegerField(choices=DEPT_CHOICES)
	is_staff=md.BooleanField(default=False)
