from django.conf.urls import url


urlpatterns = [
  	url(r'^$', 'apps.matricula.views.main', name='main'),   	
   	url(r'^matricula$', 'apps.matricula.views.matricula', name='matricula'),
   	url(r'^matricula/add$', 'apps.matricula.views.addMatricula', name='addMatricula'),
   	url(r'^curso$','apps.matricula.views.curso', name='curso'),
   	url(r'^curso/add$','apps.matricula.views.addCurso', name='addCurso'),

   	#url(r'^guardarevento$', 'apps.agenda.views.guardarEvento'),
]
