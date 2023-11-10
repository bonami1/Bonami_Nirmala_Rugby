from django.urls import path
# Import des URLs de l'interface d'administration
from django.contrib import admin
# Import des vues qui sont déclarées dans leur propre module (dossier)
from .views import HomeView, StadiumsView, TeamsView, NewsletterView, UpdateView, AboutView, api

urlpatterns = (
    path("admin", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("stadiums", StadiumsView.as_view(), name="stadiums"),
    path("teams", TeamsView.as_view(), name="teams"),
    path("newsletter", NewsletterView.as_view(), name="newsletter"),
    path("update", UpdateView.as_view(), name="update"),
    path("about", AboutView.as_view(), name="about"),
    path("api/stadiums", api.stadiumsList, name="apiStadiums"),
    path("api/stadiumsDetails/<int:pk>/", api.stadiumsListDetails, name="apiStadiumsDetails"),
    path("api/events", api.eventsList, name="apiEvents"),
    path("api/eventsDetails/<int:pk>/", api.eventsListDetails, name="apiEventsDetails"),
    path("api/teams", api.teamsList, name="apiTeams"),
    path("api/teamsDetails/<int:pk>/", api.teamsListDetails, name="apiTeamsDetails"),
    path("api/ticket/<str:pk>/",api.ticketInfos, name="apiTiketsDetails"),
)