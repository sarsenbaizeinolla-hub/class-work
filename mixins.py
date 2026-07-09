from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

# 1. Миксин, который требует логин и проверку роли (более комплексный)
class ComplexAccessMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'auth.view_user' # пример права
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        # Дополнительная логика
        return super().dispatch(request, *args, **kwargs)

# 2. Базовый миксин для примера
class BaseLoggingMixin:
    def dispatch(self, request, *args, **kwargs):
        print(f"Пользователь {request.user} зашел в {request.path}")
        return super().dispatch(request, *args, **kwargs)