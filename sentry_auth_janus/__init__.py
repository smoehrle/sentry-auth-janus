from sentry.auth import register

from .provider import JANUSOAuth2Provider

register('janus', JANUSOAuth2Provider)
