JANUS authentication for Sentry
=======================================

A single sign-on provider to let you authenticate Sentry with
Janus https://github.com/smartlgt/janus/

Install
-------

    $ pip install https://github.com/smartlgt/sentry-auth-janus/archive/master.zip


Setup
-----

Create a new Signon application with the redirect URI set to something like this:


    https://sentry.example.com/auth/sso/


Add some config to ``sentry.conf.py``:


    JANUS_SIGNON_UID = "uid"
    JANUS_SIGNON_SECRET = "secret"
    JANUS_SIGNON_BASE_DOMAIN = "https://janus.example.com"
    JANUS_SCOPE = "read"
