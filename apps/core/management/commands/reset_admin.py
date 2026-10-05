from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or reset production Django admin"

    def handle(self, *args, **options):
        User = get_user_model()

        username = "admin"
        email = "admin@example.com"
        password = "Admin@123456"

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
            },
        )

        user.email = email
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "SUCCESS: New admin user created."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "SUCCESS: Existing admin password respython manage.py runserberet."
                )
            )

        self.stdout.write(f"Username: {username}")
        self.stdout.write(f"Password: {password}")