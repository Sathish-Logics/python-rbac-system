class AccessControlService:
    def check_access(self, user, resource, permission) -> bool:
        if user.can_access(permission):
            print(
                f"ACCESS GRANTED: {user.username} -> {permission.value} on {resource.name}"
            )
            return True

        print(
            f"ACCESS DENIED: {user.username} -> {permission.value} on {resource.name}"
        )
        return False
