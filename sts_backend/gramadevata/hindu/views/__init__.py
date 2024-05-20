

from .temple_categeory_views import *
from .trmple_priority_views import *
from .goshala_category_views import *
from .event_categeory_views import*
from .goshala_views import GetIndianGoshalas, GoshalaView,GetbyStateLocationGoshalas,GetbyDistrictLocationGoshalas,GetbyBlockLocationGoshalas
from .event_views import *
from .country_views import *
from .state_views import StateViews
from .district_view import DistrictVIew
from .block_views import BlockView
from .village_views import VillageView,GetVillages
from .main_view import TempleMain,GoshalaMain, EventsMain
from .temple_views import TempleView, GetItemByfield_InputView,Templepost,GetIndianTemples,GetGlobalTemples,GetItemByfield_location,GetbyDistrictLocationTemples,GetbyBlockLocationTemples,GetbyCountryLocationTemples
from .famous_temple_view import FamousTempleListCreateView
from .comment_views import CommentView
from .register_views import Registerview,LoginApiView,VerifyOtpView,ResendOtp,ForgotOtp,ResetPassword
from .connect_views import ConnectView
from .member_views import MemberView
from .home_views import HomeView


