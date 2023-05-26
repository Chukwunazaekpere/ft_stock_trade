from rest_framework import routers
from users import viewsets as users_viewsets


app_router = routers.DefaultRouter()

app_router.register("users", users_viewsets.UsersViewSets, basename='users')
