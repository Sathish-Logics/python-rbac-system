class Role:
    def __init__(self, name: str, permissions: set):
        self.name = name
        self._permissions = permissions

    def has_permission(self, permission) -> bool:
        return permission in self._permissions