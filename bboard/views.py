from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Task

def task_list(request):
    """
    Отображает список всех задач с пагинацией по 5 штук на странице.
    """
    tasks_list = Task.objects.all().order_by('-created_at')
    paginator = Paginator(tasks_list, 5)  # 5 задач на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})