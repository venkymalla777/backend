from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash = False)
router.register('temple',TempleView)



router.register("templeCategeory",templeCategeoryview)
router.register("templepriority",TemplePriorityView)
router.register('goshalacategories', GoshalaCategoryViewSet)
router.register("eventcategory",EventCategoryView)
router.register("goshala",GoshalaView)
router.register("event",EventView)
router.register("country",CountryVIews)
router.register('state',StateViews)
router.register("district",DistrictVIew)
router.register("block",BlockView)
router.register("village",VillageView)
router.register("comment",CommentView)
router.register("famoustemples",FamousTempleListCreateView)
router.register("connect",ConnectView)
router.register("member",MemberView)
router.register("register",Registerview)
router.register("allvillages",GetVillages)



urlpatterns = [
    path('', include(router.urls)),
    path("templemain",TempleMain.as_view()),
    path("GoshalaMain",GoshalaMain.as_view()),
    path("EventsMain",EventsMain.as_view()),
    path("login",LoginApiView.as_view()),
    path("verify",VerifyOtpView.as_view()),
    path("home",HomeView.as_view()),
    path('templeget/<str:field_name>/<str:input_value>', GetItemByfield_InputView.as_view()),
    path("resend",ResendOtp.as_view()),
    path('forgot_password',ForgotOtp.as_view()),
    path("reset_password",ResetPassword.as_view()),
    path("templepost",Templepost.as_view()),
    # path('temple/by_state/<str:stateid>/', GetItemByfield_location.as_view(), name='temple-by-state'),
    path("indiatemples",GetIndianTemples.as_view()),
    path("GetIndianGoshalas",GetIndianGoshalas.as_view()),
    path("globaltemples",GetGlobalTemples.as_view()),
    path('temples/state_id/<str:state_id>/', GetItemByfield_location.as_view()),
    path('temples/district_id/<str:district_id>/', GetbyDistrictLocationTemples.as_view()),
    path('temples/block_id/<str:block_id>/', GetbyBlockLocationTemples.as_view()),
    path('temples/country_id/<str:country_id>/',GetbyCountryLocationTemples.as_view()),
    path('goshalas/state_id/<str:state_id>/', GetbyStateLocationGoshalas.as_view()),
    path('goshalas/district_id/<str:district_id>/', GetbyDistrictLocationGoshalas.as_view()),
    path('goshalas/block_id/<str:block_id>/', GetbyBlockLocationGoshalas.as_view()),
    path('Events/state_id/<str:state_id>/', GetbyStateLocationEvents.as_view()),
    path('Events/district_id/<str:district_id>/', GetbyDistrictLocationEvents.as_view()),
    path('Events/block_id/<str:block_id>/', GetbyBlockLocationEvents.as_view()),
    path('indiaevents',GetIndianEvents.as_view()),

]
