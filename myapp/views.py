from django.shortcuts import render
from django.http.response import HttpResponse

from django.shortcuts import redirect
from . import forms as fm,models as md
from accounts.models import User_info
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
def index(request):
	return render(request,'index.html')


@login_required#認証の要求
def reg_title(request):
	if request.user.is_staff==False:#ユーザーの権限を確認
		return render(request,'forbidden.html')


	form=fm.Title_reg(request.POST or None)
	if form.is_valid():
		md.Title_info.objects.create(**form.cleaned_data)
		return redirect('myapp:ls_title')

	d={
		'form':form,
		# 'title_qs':md.Title_info.objects.all().order_by('id')
	}
	return render(request,'reg_title.html',d)

@login_required#認証の要求
def reg_book(request):
	if request.user.is_staff==False:#ユーザーの権限を確認
		return render(request,'forbidden.html')
	if(request.POST.get('Title_ID')==None):
		print(request.POST)
		return HttpResponse("Reg error")
	d={
		'title':md.Book_info.objects.create(Book_ISBN=md.Title_info.objects.get(pk=request.POST.get('Title_ID')))
	}
	return render(request,'reg_book.html',d)


def ls_title(request):
	query=("SELECT * from myapp_title_info "+
			"LEFT OUTER JOIN ("+
				"SELECT Review_title_id,AVG(Review_score) AS ave "+
				"FROM myapp_review_info GROUP BY Review_title_id"+
			") AS foo ON myapp_title_info.id=foo.Review_title_id "
	)

	word=request.POST.get('title')
	if(word):
		word=str(word)
		word=word.replace('"','')
		word=word.replace("'","")
		query+='WHERE Title_name LIKE "%'+word+'%"'


	print(list(md.Title_info.objects.raw(query)))

	d={
		'title_qs':md.Title_info.objects.raw(query)
	}
	return render(request,'ls_title.html',d)


@login_required
def ls_book(request):
	d={
		'book_qs':md.Book_info.objects.all().order_by('id')
	}
	return render(request,'ls_book.html',d)

@login_required#認証の要求
def return_book(request):
	if request.user.is_staff==False:#ユーザーの権限を確認
		return render(request,'forbidden.html')
	# user_id=request.POST.get('userid_box')
	query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info)'
	Lend_data=None
	Review_form=fm.Review_form(request.POST or None)
	try:
		lend_id=request.POST.get('lendid_box')
		Lend_data=md.Lend_info.objects.get(pk=lend_id)
		md.Return_info.objects.create(Return_lend=Lend_data)
	except:
		if(lend_id):
			d={
				'form':Review_form,
				'message':"貸出記録が存在しません",
				'lend_qs':md.Lend_info.objects.raw(query)
			}
		else:
			d={
				'form':Review_form,
				'lend_qs':md.Lend_info.objects.raw(query)
			}
		return render(request,'return_book.html',d)

	d={
		'form':Review_form,
		'username':Lend_data.Lend_user.username,
		'title':Lend_data.Lend_book.Book_ISBN.Title_name,
		'lend_qs':md.Lend_info.objects.raw(query)
	}

	score=request.POST['Review_score']
	if(score):
		md.Review_info.objects.create(Review_title=Lend_data.Lend_book.Book_ISBN,Review_score=score)

	return render(request,'return_book.html',d)

@login_required
def sub_return_book(request):
	query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info)'
	if request.user.is_staff==False:#ユーザーの権限を確認
		query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info) AND Lend_user_id='+str(request.user.id)

	Lend_data=None
	Review_form=fm.Review_form(request.POST or None)
	User_ID=request.POST.get('User_ID')
	try:
		lend_id=request.POST.get('lendid_box')
		Lend_data=md.Lend_info.objects.get(pk=lend_id)
		md.Return_info.objects.create(Return_lend=Lend_data)
	except:
		if(lend_id):
			d={
				'form':Review_form,
				'message':"貸出記録が存在しません",
				'lend_qs':md.Lend_info.objects.raw(query),
				'User_ID':User_ID,
			}
		else:
			d={
				'form':Review_form,
				'lend_qs':md.Lend_info.objects.raw(query),
				'User_ID':User_ID,
			}
		return render(request,'sub_return_book.html',d)

	d={
		'form':Review_form,
		'username':Lend_data.Lend_user.username,
		'title':Lend_data.Lend_book.Book_ISBN.Title_name,
		'lend_qs':md.Lend_info.objects.raw(query),
		'User_ID':User_ID,
	}

	score=request.POST['Review_score']
	if(score):
		md.Review_info.objects.create(Review_title=Lend_data.Lend_book.Book_ISBN,Review_score=score)

	return render(request,'sub_return_book.html',d)


@login_required
def ls_lend(request):#未返却一覧
	query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info)'
	if request.user.is_staff==False:#ユーザーの権限を確認
		query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info) AND Lend_user_id='+str(request.user.id)
	d={
		'lend_qs':md.Lend_info.objects.raw(query)
	}
	return render(request,'ls_lend.html',d)


#----------------------funo------------------------
@login_required
def list_user(request):
	if request.user.is_staff==False:#ユーザーの権限を確認
		return render(request,'forbidden.html')
	message=""	
	del_id=request.POST.get('User_ID')

	if(del_id):
		if(int(del_id)!=int(request.user.id)):
			user=md.User_info.objects.get(pk=del_id)
			message="ユーザー"+str(user.username)+"を削除しました。"
			user.delete()
		else:
			message="自身を削除することはできません"

	d={
		'message':message,
		'user_qs':md.User_info.objects.all().order_by('id')
	}
	return render(request,'list_user.html',d)



@login_required
def lend_book(request):
	form=fm.Lend_reg(request.POST or None)
	message=""
	book_id=0
	user_info=request.user
	if form.is_valid():
		print('cr')
		try:
			if(user_info.is_staff):
				try:
					username=form.cleaned_data['User_ID']#入力されたusernameの取得
					user_info=md.User_info.objects.get_by_natural_key(username=username)
				except:
					message+="ユーザー名が不正です。"
					raise
			book_id=form.cleaned_data['Book_ID']#入力されたBook_IDの取得
			#入力されたBook_IDが未返却でないか確認
			query='SELECT * from myapp_lend_info WHERE id NOT IN (SELECT Return_lend_id FROM myapp_return_info) AND Lend_book_id='+str(book_id)
			qs=md.Lend_info.objects.raw(query)
			if(len(list(qs))!=0):
				message="指定された本は未返却です！\n"
				raise#未返却なら処理を中止
			#OKなら貸し出し
			print('create')
			md.Lend_info.objects.create(
				Lend_book=md.Book_info.objects.get(pk=book_id),
				Lend_user=user_info
			)

			message="貸出を受け付けました。"
		except:#例外発生時
			message+="貸出を受理できませんでした。"
	lend_qs=md.Lend_info.objects.raw("SELECT * FROM myapp_lend_info LEFT JOIN myapp_return_info ON myapp_lend_info.id=myapp_return_info.Return_lend_id")
	d={
		'form':form,
		'lend_qs':lend_qs[-10:],
		'message':message
	}
	return render(request,'lend_book.html',d)


