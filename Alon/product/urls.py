from django.urls import path

#imports the app's viewpy function 
from .views import chart_select_view

#application names
app_name = 'product'

#url patterns and paths
urlpatterns = [
    path('', chart_select_view, name='main-product-view')
]

# path step 3

# main urls -> apps urls
#
# create view -> templates -> view to urls app
