from sentry import http
from sentry.utils import json


class JANUSSignonClient(object):
    def __init__(self, client_secret, base_domain):
        self.base_domain = base_domain
        self.client_secret = client_secret
        self.http = http.build_session()

    def get_user(self, access_token):

        headers = {
            'Authorization': 'Bearer {0}'.format(access_token),
        }

        req = self.http.get(
                '{0}/o/profile/'.format(self.base_domain),
                headers=headers,
              )

        return json.loads(req.content)
