from domain.user import User


class AdminUser(User):
    def can_access(self, permission) -> bool:
        return True


class StandardUser(User):
    def can_access(self, permission) -> bool:
        return self._role.has_permission(permission)
    
class ManagerUser(User):
    def can_access(self, permission) -> bool:
        return permission.value in ["read", "write"]
