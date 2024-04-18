import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "industry_ai_agents.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import industry_ai_agents.users.signals  # noqa: F401
