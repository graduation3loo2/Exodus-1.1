from django.db.models import Count, Q
from django.shortcuts import render, redirect
from datetime import datetime

from .models import Response, Follows, Agencies, Trips, Vote


def home(request):
    votes = Vote.objects.annotate(
        interest=Count('response__interested', filter=Q(response__interested=1)),
        not_interest=Count('response__interested', filter=Q(response__interested=0))).order_by('vote_id').reverse()[:1]

    most_going = Trips.objects.filter(deadline__gt=datetime.now()).annotate(
        going=Count('activity', filter=Q(activity__type=1))).order_by('going').reverse()[:4]

    recent = Trips.objects.filter(deadline__gt=datetime.now()).annotate(
        going=Count('activity', filter=Q(activity__type=1))).order_by('trip_id').reverse()[:4]

    most_followed = Agencies.objects.annotate(followed=Count('follows')).order_by('followed').reverse()

    follows = Follows.objects.filter(user_id=4)
    followed = get_follow(most_followed, follows)

    obj = {
        'votes': votes,
        'most_going': most_going,
        'most_recent': recent,
        'most_followed': most_followed,
        'follow': followed
    }

    return render(request, 'Home.html', obj)


def vote(request):
    if request.method == 'GET':
        vote_id = request.GET.get('vote')
        user_id = 4
        interested = request.GET.get('response')
        response = Response.objects.filter(vote_id=vote_id, user_id=user_id)

        if response.count() > 0:
            response.update(vote_id=vote_id, user_id=user_id,
                            response_time=datetime.now(), interested=interested)
        else:
            Response.objects.create(vote_id=vote_id, user_id=user_id,
                                    response_time=datetime.now(), interested=interested)
    return redirect(home)


def follow(request):
    if request.method == "POST":
        user_id = 4
        agency_id = request.POST['btnFollow']
        Follows.objects.create(user_id=user_id, agency_id=agency_id)
    return redirect(home)


def un_follow(request):
    if request.method == "POST":
        user_id = 4
        agency_id = request.POST['btnUn_follow']
        Follows.objects.filter(user_id=user_id, agency_id=agency_id).delete()
    return redirect(home)


def get_follow(agencies_follow, follows):
    agency_follow = []
    for a in agencies_follow:
        followed = False
        if follows.filter(agency_id=a.agency_id).exists():
            followed = True
        following = {
                'agency': a.agency_id,
                'follow': followed
            }
        agency_follow.append(following)
    return agency_follow
