from django import template

register = template.Library()

# 1. Пункт 1: Фильтр, который обрезает строку ровно наполовину
@register.filter(name='half_cut')
def half_cut(value):
    if not isinstance(value, str):
        return value
    half_length = len(value) // 2
    return value[:half_length]

# 2. Пункт 2: Простой тег, который принимает строку и сепаратор, возвращая массив (список)
@register.simple_tag(name='split_string')
def split_string(text, separator):
    if not isinstance(text, str):
        return []
    return text.split(separator)