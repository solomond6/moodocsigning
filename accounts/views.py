from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from accounts.forms import MyRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf.urls import url
from datetime import datetime, time, timedelta
from django.utils import timezone
from .models import AppUsers
# from pylibgen import Library

import requests
import re

def loginview(request):
    context = {
        'title': 'title',
    }
    return render(request, 'accounts/login.html', context) 
    # return HttpResponse(url)




def authview(request):

    try:
    	username = request.POST.get('username', '')
    	password = request.POST.get('password', '')
    	user = AppUsers.objects.get(username=username)
    	request.session['username'] = username
    	return HttpResponseRedirect('/guarantorslist/')
    except requests.exceptions.ConnectionError:
        connection_status = "Connection refused"
        context = {
            'exception': connection_status,
        }
        # return HttpResponse(requests.exceptions)
        messages.warning(request, connection_status)
        return HttpResponseRedirect('/')
    except AssertionError as error:
        # Output expected AssertionErrors.
        # Logging.log_exception(error)
        messages.warning(request, "Username or password incorrect")
        return HttpResponseRedirect('/')
    except Exception as exception:
        # Output unexpected Exceptions.
        # Logging.log_exception(exception, False)
        context = {
            'exception': "Request Not found",
        }
        # return HttpResponse(exception)
        messages.warning(request, "Username or password incorrect")
        return HttpResponseRedirect('/')


def invalid(request):
    context = {
        'title': 'title',
    }
    return render(request, 'accounts/invalid.html', context)
    # return HttpResponse(url)


@login_required
def loggedin(request):
    context = {
        'title': 'title',
    }
    return render(request, 'accounts/dashboard.html', context)
    # return HttpResponse(url)


def logoutview(request):
    # logout(request)
    del request.session['username']
    messages.warning(request, 'Successfully Looged Out')
    return HttpResponseRedirect('/')
    


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Registration Successful. Kindly login to proceed')
			return HttpResponseRedirect('/accounts/login')
	else:
		form = MyRegistrationForm()

	args = {}
	args.update(csrf(request))
	context = {
		'form': form
	}
	return render(request, 'accounts/register.html', context)
	# return HttpResponse(form)


def register_success(request):
	context = {
		'success': 'User created successfully',
	}
	return render(request, 'accounts/register_success.html', context)
	# return HttpResponse(url)