from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Book, Author, BookInstance
from django.views import generic
from .forms import HelpForm
from .tasks import need_send_mail

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        },
    )


class BookListView(generic.ListView):
    model = Book


def contact_form_save(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            data['form_is_valid'] = True
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            need_send_mail.apply_async((subject, from_email, message))
            messages.success(request, 'Email was send successfully')
            context = {'form': form}
            data['html_form'] = render_to_string(template_name, context, request=request)
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            messages.error(request, 'Email was not send')
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def contact_form(request):
    if request.method == "POST":
        form = HelpForm(request.POST)
    else:
        form = HelpForm()
    return contact_form_save(request, form, 'catalog/help.html')
