from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
# from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, CreateView, UpdateView, DeleteView

from .models import Question, Choice
from .forms import UploadFileForm, ContactForm, ProductForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:20]
        return Question.objects.all()


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.session)
    request.session['1'] = '1'
    return render(request, 'polls/detail.html', {'question': question})


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# @require_http_methods(["POST"])
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload.html', {'form': form})


'''学习FormView代码'''


class ContactView(FormView):
    template_name = 'polls/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


'''新建Forms文件,然后到views.py下编写业务逻辑内容，并在urls.py下进行路由配置;接着新建一个template'''


class ProductListView(FormView):
    template_name = 'polls/product.html'
    form_class = ProductForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


'''学习CreateView'''


class QuestionCreate(CreateView):
    model = Question
    fields = ['question_text', 'pub_date']
    template_name = 'polls/QuestionCreate.html'
    success_url = '/polls/'


class QuestionUpdate(UpdateView):
    model = Question
    fields = ['question_text', 'pub_date']
    template_name_suffix = '_update_form'
    success_url = '/polls/'

    def get_form_kwargs(self):
        #获取kwargs对象
        kwargs = super(QuestionUpdate, self).get_form_kwargs()
        #传递参数
        kwargs.update({
            'UserID': self.kwargs['pk']

        })
        return kwargs


class QuestionDelete(DeleteView):
    model = Question
    fields = ['question_text', 'pub_date']
    template_name = 'polls/author_confirm_delete.html'
    success_url = '/polls/'