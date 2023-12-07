from django.urls import include, path, re_path
from .views import *
from django.views.decorators.cache import cache_page
# Здесь объявляем пути, а так же объеявляем функции куда переходим (функции лежат во views.py)

urlpatterns = [
    path('', index, name='home'),
    path('signIn', cache_page(15*60)(LoginUser.as_view()), name='signIn'),
    path('signUp', cache_page(60)(RegisterUser.as_view()), name='signUp'),
    path('jsonParty.json', (jsonParty), name='json'),
    path('paty/<int:pk>/updatePaty', PatyUpdate.as_view(), name='updatePaty'),
    path('paty/<int:pk>/deletePaty', PatyDelete.as_view(), name='deletePaty'),
    path('createParty', createParty, name='createParty'),
    path('mypage', mypage, name='mypage'),
    path('logout', logout_user, name='logout'),
    path('setcookie/', setcookie),
    path('getcookie/', showcookie),
    path('deletecookie/', delete_co),
    path('go', gofunc, name='gofunc'),
    # path('notgo'),
]
