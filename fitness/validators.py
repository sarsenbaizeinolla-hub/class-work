import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class RegexPasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        # Проверяем длину
        if len(password) < self.min_length:
            raise ValidationError(
                _("Пароль слишком короткий. Должно быть минимум %(min_length)d символов."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )
        
        # Проверяем регулярным выражением: нужна минимум 1 цифра, 1 заглавная и 1 строчная буква
        if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password):
            raise ValidationError(
                _("Пароль должен содержать минимум одну заглавную букву, одну строчную букву и одну цифру."),
                code='password_no_match',
            )

    def get_help_text(self):
        return _(
            "Ваш пароль должен состоять минимум из 8 символов и включать заглавные буквы, строчные буквы и цифры."
        )