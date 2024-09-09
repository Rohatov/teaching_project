from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from home.models import LessonPlans, Achievements, Videos, Photos, Category
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

def PlansView(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    plans = LessonPlans.objects.filter(category=category)
    paginator = Paginator(plans, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'plans':page_obj,
        'categories': categories
    } 
    return render(request, 'lesson-plans.html', context)


class AchievementsView(ListView):
    template_name = 'achievements.html'
    model = Achievements
    paginate_by = 3
    context_object_name = 'achievements'


class VideosView(ListView):
    template_name = 'videos.html'
    model = Videos
    paginate_by = 6
    context_object_name = 'videos'


class PhotosView(ListView):
    template_name = 'photos.html'
    model = Photos
    paginate_by = 6
    context_object_name = 'photos'

# class CategoryView(ListView):
#     template_name = 'lesson-plans.html'
#     model = Category
#     context_object_name = 'categories'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context['categories'])  # Konsolga chiqadi
#         return context

