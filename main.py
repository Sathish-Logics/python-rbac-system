from domain.permission import Permission
from domain.role import Role
from domain.resource import Resource
from domain.user_types import AdminUser, StandardUser
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.access_control_service import AccessControlService


def main():
    # Roles
    admin_role = Role("ADMIN", {Permission.READ, Permission.WRITE, Permission.DELETE})
    employee_role = Role("EMPLOYEE", {Permission.READ, Permission.WRITE})

    # Users
    admin = AdminUser(1, "admin_user", admin_role)
    employee = StandardUser(2, "employee_user", employee_role)

    # Repository
    user_repo = UserRepository()
    user_repo.add_user(admin)
    user_repo.add_user(employee)

    # Services
    auth_service = AuthService()
    access_service = AccessControlService()

    # Resource
    payroll = Resource("Payroll System")

    # Authentication & Authorization
    for user in [admin, employee]:
        if auth_service.authenticate(user):
            access_service.check_access(user, payroll, Permission.READ)
            access_service.check_access(user, payroll, Permission.WRITE)


if __name__ == "__main__":
    main()
