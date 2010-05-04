#encoding: utf-8
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^palestras/', include('talks.urls')),
    (r'', include('server.urls')),
)

talks = (
    {
    'title': 'Abertura',
    'time': '9:00',
    },
    {
    'title': '"Uma Experiência Acadêmica com Python"',
    'time': '9:20',
    'description': """
    Relato da experiência de uso da linguagem Python no Núcleo de Pesquisa em Sistemas de Informação e no ensino de programação dos cursos de computação do Instituto Federal Fluminense.
    """,
    'speaker_name': 'Fábio Duncan',
    'speaker_about': """
    Possui mestrado em Pesquisa Operacional e Inteligência Computacional pela Universidade Candido Mendes (Campos - 2008).<br />
    Atualmente é professor do Instituto Federal Fluminense e membro do Núcleo de Pesquisa em Sistemas de Informação (NSI-IFF). Tem experiência na área de Ciência da Computação com ênfase em algoritmos genéticos, programação paralela e segmentação de vídeo.
    """,
    'speaker_url': '',
    'speaker_img': '/media/images/palestrantes/fabio_duncan.jpg',
    },
    {
    'title': 'Palestra Técnica a definir',
    'time': '10:20',
    },
    {
    'title': 'Coffee Break Reforçado',
    'time': '11:20',
    },
    {
    'title': '"Computação visual com Python"',
    'time': '12:00',
    'description': """
    Você é da área de tecnologia? Acredite, você está em muita vantagem!<br />
    Conheça como funciona a sociedade e a organização do trabalho, e saiba como a Internet, o Software Livre e tecnologias como Python e Ruby podem revolucionar a sua vida.<br />
    Aprenda a hackear o "ciclo vicioso social" e ter as rédeas o teclado da sua vida, nas suas mãos.<br />
    """,
    'speaker_name': 'Jonh Edson Ribeiro de Carvalho',
    'speaker_about': 'Graduado [1997] em Física pela UFF e Mestrado [2006] em Computação também pela UFF, com Ênfase em Computação Visual e Interfaces. Professor Universitário a 10 anos, entusiasta do Movimento de Software Livre, sendo membro da SL-RJ, Debian-RJ e da PythOnRio e apoia as Culturas Livres.',
    'speaker_url': 'http://www.visual.pro.br/',
    'speaker_img': 'http://a1.twimg.com/profile_images/326997520/closecabofrio2_bigger.jpg',
    },
    {
    'title': '"Fuja da escravidão, antes que ela te alcance."',
    'time': '13:00',
    'description': """
    Você é da área de tecnologia? Acredite, você está em muita vantagem!<br />
    Conheça como funciona a sociedade e a organização do trabalho, e saiba como a Internet, o Software Livre e tecnologias como Python e Ruby podem revolucionar a sua vida.<br />
    Aprenda a hackear o "ciclo vicioso social" e ter as rédeas o teclado da sua vida, nas suas mãos.<br />
    """,
    'speaker_name': 'Vinícius Manhães Teles',
    'speaker_about': 'Desenvolvedor de software e fundador da Improve It, empresa criadora do produto web Be on the Net. Vinicius foi o pioneiro em metodologias ágeis no Brasil, realizando diversos treinamentos e palestras sobre Extreme Programming, e atuando durante muito tempo como coach de equipes XP em diversas organizações. Além disso, é autor do primeiro livro de XP do Brasil e mestre em computação pela UFRJ.',
    'speaker_url': 'http://www.improveit.com.br/',
    'speaker_img': 'http://devinrio.com.br/img/palestrante_vinicius_teles.jpg',
    },
    {
    'title': 'Palestras Relâmpago',
    'time': '14:00',
    })


urlpatterns+= patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'sobre.html'}),
    
    (r'^index2/$', 'direct_to_template', {'template': 'index2.html'}),

    (r'^sobre/$', 'direct_to_template', {'template': 'sobre.html'}),

    (r'^about/$', 'direct_to_template', {'template': 'about.html'}),

    (r'^eu-quero-uma-pythoncampus-na-minha-universidade/$',
        'direct_to_template', {'template': 'i-want.html'}),

    (r'^contato/$', 'direct_to_template', {'template': 'contact.html'}),

    (r'^making-of/$', 'direct_to_template', {'template': 'making-of.html'}),

    (r'^dojorio/$', 'direct_to_template', {'template': 'coding-dojo.html'}),

    (r'^oficina/$', 'direct_to_template', {'template': 'oficina.html'}),
    (r'^event/istcc-p/$', 'direct_to_template', {'template': 'event.html', 'extra_context': {'talks': talks} }),
    # subscription
    (r'^event/istcc-p/', include('subscription.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
