from django.urls import path, include
from rest_framework import routers
from . import views

# router 路由器(總機小姐)
router = routers.DefaultRouter()

#配對 path 與 view(分機小姐)
# http://127.0.0.1:8000/food
router.register(r'food',views.FoodViewSet)
#設定 總機小姐 路由(2組)
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/api
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),

]