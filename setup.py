"""
sentry-auth-janus
==================
:copyright: (c) 2017 Smart LGT GmbH
"""

from setuptools import find_packages, setup

install_requires = [
    'sentry>=7.0.0',
]

setup(
    name='sentry-auth-janus',
    version='0.0.1',
    description="sentry auth service for janus sso",
    url='https://github.com/fachschaft/sentry-auth-janus/',
    author='Smart LGT GmbH',
    author_email='support@smart-lgt.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    keywords='sentry',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.apps': [
            'auth_janus = sentry_auth_janus',
        ],
    },
)
