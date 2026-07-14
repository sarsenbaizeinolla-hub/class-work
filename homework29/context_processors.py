def user_groups_context(request):
    """
    Контекстный процессор, который автоматически добавляет список групп 
    текущего пользователя во все HTML-шаблоны сайта.
    """
    # Проверяем, авторизован ли пользователь на сайте
    if request.user.is_authenticated:
        # Забираем все имена групп, в которых состоит пользователь, в виде списка строк
        groups = list(request.user.groups.values_list('name', flat=True))
    else:
        # Если пользователь — гость, список групп пустой
        groups = []
        
    # Возвращаем словарь. Ключ 'user_groups' станет доступен во всех HTML файлах
    return {
        'user_groups': groups
    }