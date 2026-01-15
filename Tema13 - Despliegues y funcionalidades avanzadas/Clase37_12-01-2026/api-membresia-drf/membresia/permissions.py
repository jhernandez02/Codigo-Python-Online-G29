from rest_framework.permissions import BasePermission

class IsNotSuperUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated 
            and not request.user.is_superuser
        )

class BlockUpdate(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method in ['PUT','PATCH']:
            return False
        return True

class BlockDelete(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method in ['DELETE']:
            return False
        return True