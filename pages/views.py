from django.shortcuts import render
from django.http import HttpResponse
from workshops.models import Workshop
from facilitators.models import Facilitator
from workshops.choices import bedroom_choices , price_choices , state_choices
def index(request):
    workshops = Workshop.objects.order_by('-workshop_date').filter(is_published=True)[:3]
    context={
        'workshops':workshops,
        # 'bedroom_choices' :bedroom_choices,
        # 'price_choices': price_choices,
        # 'state_choices':state_choices


    }
    return render(request,'pages/index.html', context)

def about(request):
    # get all the facilitators
    facilitators= Facilitator.objects.order_by('-join_date')
    # get mvp
    mvp_facilitators= Facilitator.objects.all().filter(is_mvp=True)
    context= {
        'facilitators':facilitators,
        'mvp_facilitators':mvp_facilitators
    }
    return render(request,'pages/about.html', context)
