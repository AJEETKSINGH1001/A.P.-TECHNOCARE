from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Reset/list Django admin users"

    def handle(self, *args, **options):
        User = get_user_model()

        self.stdout.write("\n=== Django Users ===")

        for user in User.objects.all():
            self.stdout.write(
                f"Username: {user.username} | "
                f"Email: {user.email} | "
                f"Active: {user.is_active} | "
                f"Staff: {user.is_staff} | "
                f"Superuser: {user.is_superuser}"
            )

        self.stdout.write("\n=== Resetting admin user ===")

        username = "admin"
        password = "admin@123"

        try:
            user = User.objects.get(username=username)

            user.set_password(password)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"SUCCESS: Password reset for {username}"
                )
            )

        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    f"ERROR: User '{username}' does not exist."
                )
            )