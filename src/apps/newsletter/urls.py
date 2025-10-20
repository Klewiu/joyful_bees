from django.urls import path
from django.http import HttpResponse


def _newsletter_disabled(request, *args, **kwargs):
    # Safe placeholder while newsletter is turned off.
    return HttpResponse("Przepraszamy - Newsletter chwilowo nieczynny, prosimy o wiadomość emial.", content_type="text/plain", status=200)


urlpatterns = [
    path('newsletter_user_list/', _newsletter_disabled, name='newsletter_user_list-view'),
    path('newsletter/', _newsletter_disabled, name='newsletter'),
    path('runletter/', _newsletter_disabled, name='runletter'),
    path('confirm/', _newsletter_disabled, name='confirm'),
    path('delete/', _newsletter_disabled, name='delete'),
]