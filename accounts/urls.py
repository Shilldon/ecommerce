from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"), # the name is what it is referred to in the html, the second argument (registration) is what it is called in the view
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]    