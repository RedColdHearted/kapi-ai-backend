from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AssistantsAppConfig(AppConfig):
    """Default configuration for Assistants app."""

    name = "apps.assistants"
    verbose_name = _("Assistants")

    def ready(self) -> None:
        from .api import scheme  # noqa
