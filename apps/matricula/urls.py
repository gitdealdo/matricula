from django.conf.urls import url


urlpatterns = [
  	url(r'^$', 'apps.matricula.views.main', name='main'),   	
   	#url(r'^agendamain$', 'apps.agenda.views.agendamain', name='agendamain'),
   	#url(r'^usuarios$', 'apps.agenda.views.usuarios', name='usuarios'),
   	#url(r'^institucion$','apps.agenda.views.institucion', name='institucion'),

   	#url(r'^guardarevento$', 'apps.agenda.views.guardarEvento'),
]
