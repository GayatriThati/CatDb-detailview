from django.urls import path
from django.conf.urls import url

#from .views import HomeList,HumanList,BreedList,CatList
from .views import IndexList,HomeDetail

urlpatterns = [
    #path('home/', HomeList.as_view()), # template name should be 'home_list' or Home_list!
    #path('human/', HumanList.as_view()),
    #path('breed/', BreedList.as_view()),
    #path('cat/', CatList.as_view()),
    path('', IndexList.as_view()),
    path('<pk>', HomeDetail.as_view()),
    #url(r'^(?P<slug>[\w-]+)/(?P<pk>[0-9]+)$', HomeDetail.as_view())
]

