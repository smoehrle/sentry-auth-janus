from django.conf import settings

CLIENT_ID = getattr(settings, 'JANUS_SIGNON_UID', None)
CLIENT_SECRET = getattr(settings, 'JANUS_SIGNON_SECRET', None)

BASE_DOMAIN = getattr(settings, 'JANUS_SIGNON_BASE_DOMAIN', None)
SCOPE = getattr(settings, 'JANUS_SCOPE', None)

ACCESS_TOKEN_URL = '{0}/o/token/'.format(BASE_DOMAIN)
AUTHORIZE_URL = '{0}/o/authorize/'.format(BASE_DOMAIN)
