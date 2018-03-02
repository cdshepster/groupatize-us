from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import smtplib
from .models import User
import hashlib
import sha3

def index(request):
	#print "Main page!"
	
	context = {'login_success':request.GET.get('login_success'),
				'logout_success':request.GET.get('logout_success'),
				'email_in_use':request.GET.get('email_in_use'),
				'create_account':request.GET.get('create_account')
				}
	
	#s=smtplib.SMTP("smtp.gmail.com", 587)
	#s.ehlo()
	#s.starttls()
	#s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
	#to_email = "groupatizer@gmail.com"
	#msg = '\r\n'.join(['Subject: Test Subject 2', "", "this is the body 2"])
	#s.sendmail(EMAIL_HOST_USER, to_email, msg)
				
	return render(request, 'mainApp/index.html', context)


def login(request):
	#print "Entered login processing"
	# get username and password
	email = request.POST['email'].strip()
	password = request.POST['password'].strip()

	# hash password
	s = hashlib.sha3_256()
	s.update(password)
	password = s.hexdigest()

	# search for account associated with Email
	results = User.objects.filter(email=email)

	# if we found the account
	if len(results) == 1 and results[0].password == password:
		# log them in
		request.session['user'] = results[0].pk
		#send them back
		return redirect('../?login_success=True')
	else:
		return redirect('../?login_success=False')

def logout(request):
	#print "logout"
	request.session['user'] = None
	return redirect('../?logout_success=True')

def create_account(request):
	#print "Create account!"
	# get form data
	first_name = request.POST['first_name'].strip()
	last_name = request.POST['last_name'].strip()
	email = request.POST['email'].strip()
	password = request.POST['password']
	full_name = first_name + " " + last_name

	# check if that email is already associated with an account
	results = User.objects.filter(email=email)

	# if theres already an account with that email then return an error
	if len(results) > 0:
		return redirect('../?email_in_use=True')

	# hash password
	s = hashlib.sha3_256()
	s.update(password)
	password = s.hexdigest()
	print s.hexdigest()

	#create the user
	user = User(name=full_name, email=email, password=password)
	user.save()

	#log the user in
	request.session['user'] = user.pk

	# return
	return redirect('../?create_account=True')

def redir_create_event_page(request):
	#print "Redirect create event"

	if request.GET.get('email_in_use') == 'True':
		context = {'event_name':request.GET.get('event_name'),
					'first_name':request.GET.get('first_name'),
					'last_name':request.GET.get('last_name'),
					'email_in_use':'True',
					'description':request.GET.get('description'),
					'preffered_size':request.GET.get('preffered_size')
					}
	else:
		# get form data
		event_name = request.POST.get('event_name', "")
		context = {'event_name':event_name}
	return render(request, 'mainApp/createEvent.html', context)

def create_event(request):
	#print "Create event"
	# get form data
	event_name = request.POST['event_name']
	description = request.POST['description']
	preffered_size = request.POST['preffered_size']
	#print "Creating event"

	if request.session['user'] != None:
		print "user logged in"
		user = User.objects.filter(pk=request.session['user'])[0]
		user.create_event(event_name, description, preffered_size)
	else:
		# get form data
		first_name = request.POST['first_name'].strip()
		last_name = request.POST['last_name'].strip()
		email = request.POST['email'].strip()
		password = request.POST['password']
		full_name = first_name + " " + last_name

		# check if that email is already associated with an account
		results = User.objects.filter(email=email)

		# if theres already an account with that email then return an error
		if len(results) > 0:
			return redirect('../?email_in_use=True&first_name='+first_name+'&last_name='+last_name+
			'&email='+email+'&preffered_size'+ preffered_size + '&description='+description)

		# hash password
		s = hashlib.sha3_256()
		s.update(password)
		password = s.hexdigest()

		#create the user
		user = User(name=full_name, email=email, password=password)
		user.save()

		#log the user in
		request.session['user'] = user.pk

		#create the event
		user.create_event(event_name, description, preffered_size)
	return redirect(reverse('index'))
