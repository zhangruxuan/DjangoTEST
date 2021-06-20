from django.http import HttpResponse,HttpResponseRedirect
from django.urls import path
from django.template import loader
POST_FORM = '''
<form method='POST' action='/test_get_post'>
	用户名：<input type='text' name='uname'>
	<input type="submit" value="提交按钮">
</form>
'''

def page_2003_view(request):
	html = "<h1>这是第一个页面<h1>"
	return HttpResponse(html)

def index_view(request):
	html = "<h1>这是我的首页<h1>"
	return HttpResponse(html)

def page1_view(request):
	html = "<h1>这是编号唯一的网页<h1>"
	return HttpResponse(html)

def page2_view(request):
	html = "<h1>这是编号为二的网页<h1>"
	return HttpResponse(html)

def pagen_view(request, pg):
	html = '这是编号为%s的网页'%(pg)
	return HttpResponse(html)

def cal_view(request,n,op,m):
	if(op not in ['add', 'sub', 'mul']):
		return HttpResponse('your op is wrong')
	result = 0
	if op == 'add':
		result = n + m
	if op == 'sub':
		result = n - m
	if op == 'mul':
		result = n * m
	html = '结果为%s'%(result)
	return HttpResponse(html)

def cal2_view(request, x, op, y):
	html = 'x:%s op:%s y:%s'%(x, op , y)
	return HttpResponse(html)

def bir_view(request, year, mon, day):
	html = '生日为：%s年%s月%s日'%(year, mon, day)
	return HttpResponse(html)

def redi_view(request):
	return HttpResponseRedirect('/page/1')

def test_get_post(request):
	if request.method == 'GET':
		# print(request.GET)
		# print(request.GET['A'])
		# print(request.GET.get('C', 'NO C'))
		# print(request.GET.getlist('A'))
		return HttpResponse(POST_FORM)
	elif request.method == 'POST':
		#处理用户提交数据
		print('uname is', request.POST['uname'])
		return HttpResponse('POST IS OK')
	else:
		pass
	return HttpResponse('--TEST GET POST IS OK--')

def test_html(request):
	# #1.通过loader加载模板
	# t = loader.get_template('test_html.html')
	# #2.将loader转成HTML字符串（）
	# html = t.render()
	# #3.用响应对象将转换的字符串内容返回给浏览器
	# return HttpResponse(html)
	from django.shortcuts import  render
	dic = {'username':'zhangruxuan','age':'18'}
	return render(request, 'test_html.html',dic)

def say_hi():
	return 'hhhhhhh'
class Dog:
	def say(self):
		return 'wangwangwang'
def test_html_param(request):
	from django.shortcuts import render
	dic = {}
	dic['int'] = 88
	dic['str'] = 'zhangruxuan'
	dic['lst'] = ['Tom', 'Jack', 'Lily']
	dic['dict'] = {'a':9, 'b':8}
	dic['func'] = say_hi
	dic['class_obj'] = Dog()
	return render(request, 'test_html_param.html', dic)

def test_if_for(request):