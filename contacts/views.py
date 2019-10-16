from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    workshop_id = request.POST['workshop_id']
    workshop = request.POST['workshop']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    facilitator_email = request.POST['facilitator_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(workshop_id=workshop_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this workshop')
        return redirect('/workshops/'+workshop_id)

    contact = Contact(workshop=workshop, workshop_id=workshop_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()
    # Send email
    send_mail(
        'Property workshop Inquiry',
        'There has been an inquiry for ' + workshop + '. Sign into the admin panel for more info',
        'traversy.brad@gmail.com',
        [facilitator_email, 'sujitsingh1001@gmail.com'],
        fail_silently=False
    )
    messages.success(request, 'Your request has been submitted, a facilitator will get back to you soon')
    return redirect('/workshops/'+workshop_id)