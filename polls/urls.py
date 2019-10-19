from django.urls import path
from django.views.generic import ArchiveIndexView

from polls.models import Question
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('upload/', views.upload_file, name='upload_file'),
    path('form/', views.get_name, name='form'),
    path('formview/', views.ContactView.as_view(), name='formview'),
    path('product/', views.ProductListView.as_view(), name='productList'),
    path('create/', views.QuestionCreate.as_view(), name='QuestionCreate'),
    path('update/<int:pk>/', views.QuestionUpdate.as_view(), name='QuestionUpdate'),
    path('delete/<int:pk>/', views.QuestionDelete.as_view(), name='QuestionDelete'),
    # 通用日期视图
    path('archive/',
         ArchiveIndexView.as_view(model=Question, date_field="pub_date"),
         name="question_archive"),
    # 学习formset
    path('manage_article/', views.manage_article, name='manage_article'),
]

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]