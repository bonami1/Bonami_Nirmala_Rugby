from django.views.generic import TemplateView
from mainapp.models import Event, Stadium, Team, Ticket
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def eventsList(requets):
    event = Event.objects.all()
    data = {"RESULT" : list(event.values("stadium", "team_home", "team_away", "start"))}
    return JsonResponse(data)

def eventsListDetails(request, pk):
    events = get_object_or_404(Event, pk=pk)
    stadiums = events.stadium
    team_home = events.team_home
    team_away = events.team_away

    # comme dans le model Event il y a 3 foreignKey il faut les infos de : stadiums, team_home et team_away
    stadium_data = {
        "name": stadiums.name,
        "location": stadiums.location,
        "latitude": stadiums.latitude,
        "longitude": stadiums.longitude
    }

    team_home_data = {
        "country": team_home.country,
        "country_alpha2": team_home.country_alpha2,
        "nickname": team_home.nickname,
        "color_first": team_home.color_first,
        "color_second": team_home.color_second
    }

    team_away_data = {
        "country": team_away.country,
        "country_alpha2": team_away.country_alpha2,
        "nickname": team_away.nickname,
        "color_first": team_away.color_first,
        "color_second": team_away.color_second
    }

    data = {"results" : {
        "stadium" : stadium_data,
        "team_home" : team_home_data,
        "team_away" : team_away_data,
        "start" : events.start # events.start.isoformat()
    }}
    return JsonResponse(data)

def teamsList(requets):
    team = Team.objects.all()
    data = {"RESULT" : list(team.values("country", "country_alpha2", "nickname", "color_first", "color_second"))}
    return JsonResponse(data)

def teamsListDetails(request, pk):
    teams = get_object_or_404(Team, pk=pk)
    data = {"result": {
        "country": teams.country,
        "country_alpha2": teams.country_alpha2,
        "nickname": teams.nickname,
        "color_first": teams.color_first,
        "color_second": teams.color_second
    }}
    return JsonResponse(data)

def stadiumsList(requets):
    stadium = Stadium.objects.all()
    data = {"RESULT": list(stadium.values("name", "location", "latitude", "longitude"))}
    return JsonResponse(data)

def stadiumsListDetails(request, pk):
    stadiums = get_object_or_404(Stadium, pk=pk)
    data = {"result": {
        "name": stadiums.name,
        "location": stadiums.location,
        "latitude": stadiums.latitude,
        "longitude": stadiums.longitude
    }}
    return JsonResponse(data) # return render()

def ticketInfos(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    #ticket = Ticket.objects.get_by_uuid(ticket_id)
    event_data = eventsListDetails(request, pk=ticket.pk)
    
    ticket_data = {"results" : {
        "id": ticket.id,
        "event": {
            "stadium": event_data["result"]["stadium"],
            "team_home": event_data["result"]["team_home"],
            "team_away": event_data["result"]["team_away"]
        },
        "category": ticket.category,
        "seat": ticket.seat,
        "price": ticket.price,
        "currency": ticket.currency
    }}
    return JsonResponse(ticket_data)
