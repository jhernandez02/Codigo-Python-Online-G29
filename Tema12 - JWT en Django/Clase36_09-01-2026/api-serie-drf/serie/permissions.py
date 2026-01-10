from rest_framework.permissions import  BasePermission

class IsNotSuperUser(BasePermission):
    # Permite acceso solo a usuarios autenticasdos que NO sean administrador
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated   # que el usuario este autenticado
            and not request.user.is_superuser   # que no sea un administrador
        )