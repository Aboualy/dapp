from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from accounts.signals import create_profile, save_profile


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals

