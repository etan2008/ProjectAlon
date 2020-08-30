from django.urls import path

#imports the app's viewpy function
from .views import stats_view

#application names
app_name = 'statistics'

#url patterns and paths
urlpatterns = [
    path('', stats_view, name='stats-view')
]

# path step 3

# main urls -> apps urls
#
# create view -> templates -> view to urls app
