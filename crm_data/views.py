from django.shortcuts import render, redirect
from crm_data.forms import UserForm, ProfileForm
from crm_data.forms import *
from crm_data import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import CallingSheet, Interested, Escalation, PaymentConfirmation, PaymentDone










def dummy(request):
	return render(request,'dummy.html')

def home(request):
	if request.session.get('username'):
		username=request.session.get('username')
		d={'username':username}
		return render(request,'home.html',d)
	return render(request,'home.html')

def registration(request):
	UO=UserForm()
	PO=ProfileForm()
	d={'UO':UO,'PO':PO}

	if request.method=='POST' and request.FILES:
		UFD=UserForm(request.POST)
		PFD=ProfileForm(request.POST,request.FILES)
		if UFD.is_valid() and PFD.is_valid():
			UFO=UFD.save(commit=False)
			pw=UFD.cleaned_data['password']
			UFO.set_password(pw)
			UFO.save()

			PFO=PFD.save(commit=False)
			PFO.username=UFO
			PFO.save()
			return HttpResponse('registration is succeffull')
		else:
			return HttpResponse('invalid data')


	return render(request,'registration.html',d)



def user_login(request):
	if request.method=='POST':
		username=request.POST['un']
		password=request.POST['pw']

		AUO=authenticate(username=username,password=password)
		if AUO and AUO.is_active:
			login(request,AUO)
			request.session['username']=username
			return HttpResponseRedirect(reverse('crm_data:home'))
		else:
			return HttpResponse('invalid login Creditials')
	return render(request,'user_login.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('crm_data:home'))

def contact_us(request):
	return render(request,'contact_us.html')

def about_us(request):
	return render(request,'about_us.html')

def profile(request):
	username=request.session.get('username')
	UO=User.objects.get(username=username)
	PO=Profile.objects.get(username=UO)
	d={'UO':UO,'PO':PO}
	return render(request,'profile.html',d)

@login_required
def callingsheet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        product_name = request.POST.get('product_name')
        associate_name = request.POST.get('associate_name')
        location = request.POST.get('location')
        feedback = request.POST.get('feedback')
        CallingSheet.objects.create(
            name=name,
            mobile_no=mobile_no,
            product_name=product_name,
            associate_name=associate_name,
            location=location,
            feedback=feedback
        )
        return redirect('crm_data:callingsheet')
    calset = CallingSheet.objects.all()
    return render(request, 'callingsheet.html', {'calset': calset})


@login_required
def intrested(request):
	intro = Interested.objects.all()
	return render(request, 'intrested.html',{'intro': intro})

@login_required
def escalation(request):
	escu = Escalation.objects.all()
	return render(request, 'escalation.html',{'escu': escu})

@login_required
def paymentconfirmation(request):
	paym = PaymentConfirmation.objects.all()
	return render(request,'paymentconfirmation.html',{'paym': paym})

@login_required
def paymentdone(request):
	payd = PaymentDone.objects.all()
	return render(request,'paymentdone.html',{'payd': payd})
	

def move_to_interested(request, id):
    obj = get_object_or_404(CallingSheet, id=id)
    Interested.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:callingsheet')

def move_to_escalation(request, id):
    obj = get_object_or_404(CallingSheet, id=id)
    Escalation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
        payment_explanation=""
    )
    obj.delete()
    return redirect('crm_data:callingsheet')

def move_to_payment_confirmation(request, id):
    obj = get_object_or_404(CallingSheet, id=id)
    PaymentConfirmation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:callingsheet')

def move_to_payment_done(request, id):
    obj = get_object_or_404(CallingSheet, id=id)
    PaymentDone.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:callingsheet')



def interested_to_callingsheet(request, id):
    obj = get_object_or_404(Interested, id=id)
    CallingSheet.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:intrested')

def interested_to_escalation(request, id):
    obj = get_object_or_404(Interested, id=id)
    Escalation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
        payment_explanation=""
    )
    obj.delete()
    return redirect('crm_data:intrested')

def interested_to_payment_confirmation(request, id):
    obj = get_object_or_404(Interested, id=id)
    PaymentConfirmation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:intrested')

def interested_to_payment_done(request, id):
    obj = get_object_or_404(Interested, id=id)
    PaymentDone.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback
    )
    obj.delete()
    return redirect('crm_data:intrested')




@login_required
def move_escalation_to_interested(request, pk):
    escalation = get_object_or_404(Escalation, pk=pk)
    Interested.objects.create(
        name=escalation.name,
        mobile_no=escalation.mobile_no,
        product_name=escalation.product_name,
        associate_name=escalation.associate_name,
        location=escalation.location,
        feedback=escalation.feedback,
    )
    escalation.delete()
    return redirect('crm_data:escalation')


@login_required
def move_escalation_to_callingsheet(request, pk):
    escalation = get_object_or_404(Escalation, pk=pk)
    CallingSheet.objects.create(
        name=escalation.name,
        mobile_no=escalation.mobile_no,
        product_name=escalation.product_name,
        associate_name=escalation.associate_name,
        location=escalation.location,
        feedback=escalation.feedback,
    )
    escalation.delete()
    return redirect('crm_data:escalation')


@login_required
def move_escalation_to_payment_confirmation(request, pk):
    escalation = get_object_or_404(Escalation, pk=pk)
    PaymentConfirmation.objects.create(
        name=escalation.name,
        mobile_no=escalation.mobile_no,
        product_name=escalation.product_name,
        associate_name=escalation.associate_name,
        location=escalation.location,
        feedback=escalation.feedback,
    )
    escalation.delete()
    return redirect('crm_data:escalation')


@login_required
def move_escalation_to_payment_done(request, pk):
    escalation = get_object_or_404(Escalation, pk=pk)
    PaymentDone.objects.create(
        name=escalation.name,
        mobile_no=escalation.mobile_no,
        product_name=escalation.product_name,
        associate_name=escalation.associate_name,
        location=escalation.location,
        feedback=escalation.feedback,
    )
    escalation.delete()
    return redirect('crm_data:escalation')


@login_required
def paymentconfirmation_to_callingsheet(request, pk):
    obj = get_object_or_404(PaymentConfirmation, pk=pk)
    CallingSheet.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentconfirmation')


@login_required
def paymentconfirmation_to_interested(request, pk):
    obj = get_object_or_404(PaymentConfirmation, pk=pk)
    Interested.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentconfirmation')


@login_required
def paymentconfirmation_to_escalation(request, pk):
    obj = get_object_or_404(PaymentConfirmation, pk=pk)
    Escalation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
        payment_explanation=""
    )
    obj.delete()
    return redirect('crm_data:paymentconfirmation')


@login_required
def paymentconfirmation_to_payment_done(request, pk):
    obj = get_object_or_404(PaymentConfirmation, pk=pk)
    PaymentDone.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentconfirmation')


@login_required
def paymentdone_to_callingsheet(request, pk):
    obj = get_object_or_404(PaymentDone, pk=pk)
    CallingSheet.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentdone')


@login_required
def paymentdone_to_interested(request, pk):
    obj = get_object_or_404(PaymentDone, pk=pk)
    Interested.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentdone')


@login_required
def paymentdone_to_escalation(request, pk):
    obj = get_object_or_404(PaymentDone, pk=pk)
    Escalation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
        payment_explanation=""
    )
    obj.delete()
    return redirect('crm_data:paymentdone')


@login_required
def paymentdone_to_paymentconfirmation(request, pk):
    obj = get_object_or_404(PaymentDone, pk=pk)
    PaymentConfirmation.objects.create(
        name=obj.name,
        mobile_no=obj.mobile_no,
        product_name=obj.product_name,
        associate_name=obj.associate_name,
        location=obj.location,
        feedback=obj.feedback,
    )
    obj.delete()
    return redirect('crm_data:paymentdone')


