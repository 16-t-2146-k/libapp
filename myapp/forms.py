from django import forms

DEPT_CHOICES=(
	(10,"工学部"),
	(20,"教育学部"),
	(99,"管理課")
)

class Book_reg(forms.Form):
	Book_name=forms.CharField(
		label="本の名前",
		max_length=30,
		required=True,
		widget=forms.TextInput()
	)
class Title_reg(forms.Form):
	Title_name=forms.CharField(
		label="本のタイトル",
		max_length=50,
		required=True,
		widget=forms.TextInput()
	)
	Title_ISBN=forms.CharField(
		label="ISBNなど",
		max_length=30,
		required=True,
		widget=forms.TextInput()
	)

class User_reg(forms.Form):
	User_name=forms.CharField(
		label="氏名",
		max_length=20,
		required=True,
		widget=forms.TextInput()
	)
	User_ID=forms.CharField(
		label="ID",
		max_length=10,
		required=True,
		widget=forms.TextInput()
	)
	Dept_code=forms.ChoiceField(
		label="部局",
		required=True,
		widget=forms.Select,
		choices=DEPT_CHOICES
	)
#funo

class User_id(forms.Form):
	User_ID=forms.CharField(
		label="ID",
		max_length=10,
		required=True,
		widget=forms.TextInput()
	)

# class Lend_reg(forms.Form):
# 	Book_name=forms.CharField(
# 		label="本の名前",
# 		max_length=30,
# 		required=True,
# 		widget=forms.TextInput()
# 	)
# 	User_ID=forms.CharField(
# 		label="ID",
# 		max_length=10,
# 		required=True,
# 		widget=forms.TextInput()
# 	)

class Lend_reg(forms.Form):

	Book_ID=forms.IntegerField(
		label="本のID",
		required=True,
		widget=forms.TextInput()
	)

	User_ID=forms.CharField(
		label="ユーザー名",
		required=False,
		widget=forms.TextInput()
	)

class Return_reg(forms.Form):
	Lend_ID=forms.IntegerField(
		label="貸出ID",
		required=True,
		widget=forms.TextInput()
	)

class Review_form(forms.Form):
	SCORE_CHOICES=(
		(None,"無回答"),
		(1,"おすすめしない"),
		(2,"あまりおすすめしない"),
		(3,"どちらでもない"),
		(4,"おすすめする"),
		(5,"強くおすすめする"),
	)
	Review_score=forms.ChoiceField(
		label="評価",
		required=False,
		choices=SCORE_CHOICES,
		widget=forms.Select
	)
