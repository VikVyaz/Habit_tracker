from rest_framework.permissions import SAFE_METHODS, BasePermission


class HabitPermission(BasePermission):
    """Пермишн для привычек:
    - Каждый пользователь имеет доступ только к своим привычкам.
    - Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True

        if request.method in SAFE_METHODS and obj.is_public:
            return True

        return False
