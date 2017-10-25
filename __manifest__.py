# -*- coding: utf-8 -*-
{
    'name': 'Okta OAuth',
    'version': '10.0',
    'author': 'OdooGap',
    'summary': 'Okta OAuth Module',
    'description': 'Okta OAuth specifics module',
    'website': 'https://www.odoogap.com',
    'category': 'Authentication',
    'depends': [
        'auth_oauth',
    ],
    'data': [
        'data/auth_oauth_provider_data.xml',
        'data/auto_signup_data.xml',
        'views/signup.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
