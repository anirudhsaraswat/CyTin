from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Software
from .models import News
from .tags import getTags

import sendgrid
import os
from sendgrid.helpers.mail import *
# Create your views here.

def home(request):
	# The User who is logged in
	# print(request.user)
	query = Software.objects.all()
	for item in query:
		item.category = list(getTags(item.category))
	context = {
		"item_list" : query,
		"active" : "home",
	}
	return render(request, "home.html", context)

def test(request, id):
	res = "<h1>Hello World </h1>"
	return HttpResponse(res)

def details(request, id):
	query = Software.objects.filter(pk=id)
	for item in query:
		item.category = (getTags(item.category))
	context = {
		"items" : query,
		"active" : "home",
	}
	return render(request, "details.html", context)

def categories(request):
	query = Software.objects.all()
	res_str = ""
	for q in query:
		res_str += (" " + (q.category))
	tags = getTags(res_str)

	context = {
		"tags" : tags,
		"active" : "categories",
	}
	
	# print(context)
	return render(request, "categories.html", context)
	# return test(request, 1)

def newlyadded(request):
	query = Software.objects.all().order_by("-timestamp")
	for item in query:
		item.category = getTags(item.category)
	context = {
		"item_list" : query,
		"active" : "newlyadded",
	}
	# print(context)
	return render(request, "home.html", context)
	# return test(request, 1)

def majoros(request):
	query = Software.objects.filter(isos=True)
	for item in query:
		item.category = getTags(item.category)
	context = {
		"item_list" : query,
		"active" : "majoros",
	}
	# print(context)
	return render(request, "home.html", context)
	# return test(request, 1)

def news(request):
	query = News.objects.all().order_by("-timestamp")

	context = {
		"news_list" : query,
		"active" 	: "news",
	}

	return render(request, "news.html", context)

def news_details(request, id):
	query = News.objects.filter(pk=id)
	context = {
		"news" : query,
		"active" : "news",
	}

	return render(request, "news_details.html", context)

def requested(request):
	query = Software.objects.filter(isRequested=True).order_by("-timestamp")
	for item in query:
		item.category = getTags(item.category)
	context = {
		"item_list" : query,
		"active" 	: "requested",
	}

	return render(request, "home.html", context)

def bycategories(request, category):
	query = Software.objects.filter(category__icontains=category)
	# print(query)
	for item in query:
		item.category = getTags(item.category)
	context = {
		"item_list" : query,
		"active" 	: "home",
	}

	return render(request, "home.html", context)

def sendmail_view(request):
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	print(os.environ.get("SENDGRID_API_KEY"))
	from_email = Email("iamoneofmykind@gmail.com")
	to_email = Email("iamoneofmykind@gmail.com")
	subject = "Sending with SendGrid is Fun"
	content = Content("text/plain", "and easy to do anywhere, even with Python")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)
	return HttpResponse("<h1>Mail Sent</h1>")