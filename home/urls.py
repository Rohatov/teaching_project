from django.urls import path
from home.views import HomeView, PlansView, AchievementsView, VideosView, PhotosView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lesson-plans/<int:id>/', PlansView, name='plans'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('videos/', VideosView.as_view(), name='videos'),
    path('photos/', PhotosView.as_view(), name='photos'),
]