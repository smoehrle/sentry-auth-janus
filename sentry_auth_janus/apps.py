from __future__ import absolute_import

from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry_auth_janus"
    label = 'custom_auth_janus' 

    def ready(self):
        from sentry.auth import register

        from .provider import JANUSOAuth2Provider

        register('janus', JANUSOAuth2Provider)
