from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import workshop
from workshops.choices import bedroom_choices , price_choices , state_choices


def workshops(request):
    workshops= workshop.objects.order_by('-workshop_date').filter(is_published=True)
    # pagination
    paginator = Paginator(workshops, 3)
    page= request.GET.get('page')
    paged_workshops= paginator.get_page(page)

    context={
        "workshops":paged_workshops
    }
    return render(request,'workshops/workshops.html',context)
def workshop(request, workshop_id):
    workshop= get_object_or_404(workshop, pk=workshop_id)
    context={
        'workshop':workshop
    } 
    return render(request,'workshops/workshop.html', context)
def search(request):
    queryset_list= workshop.objects.order_by('-workshop_date').filter()
    # keywords

    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            queryset_list= queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            queryset_list= queryset_list.filter(city__iexact=city)
    if 'state' in request.GET:
        state= request.GET['state']
        if state:
            queryset_list= queryset_list.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms:
            queryset_list= queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            queryset_list= queryset_list.filter(price__lte=price)
    
    


    context={
        'workshops':queryset_list,
        'bedroom_choices' :bedroom_choices,
        'price_choices': price_choices,
        'state_choices':state_choices,
        'values':request.GET

    }
    return render(request,'workshops/search.html', context)
    