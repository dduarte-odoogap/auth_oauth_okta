# -*- coding: utf-8 -*-
from odoo import fields, models, _
import requests

from odoo.exceptions import UserError
import json


class AuthOAuthProvider(models.Model):
    _inherit = 'auth.oauth.provider'

    client_secret = fields.Char(string=_('Client Secret'))

    def get_okta_oauth_provider(self):
        return self.env['auth.oauth.provider'].sudo().search([
            ('id', '=', self.env.ref('smart_shop_oauth.auth_oauth_provider_okta').id),
        ], limit=1)

    def create_okta_oauth_client(self, access_token, uuid, subdomain_name):
        url = self.env['ir.config_parameter'].get_param('okta_oauth.url_api_users_clients')
        params = {
            'userID': uuid,
            'name': subdomain_name,
            'redirect': 'https://%s/auth_oauth/signin' % subdomain_name,
        }
        headers = {'Authorization': 'Bearer %s' % access_token}

        f = requests.post(url=url, params=params, headers=headers)
        response = f.content
        response = json.loads(response)

        if response.get('error'):
            raise UserError(_('Could not create the client: %s') % response)

        return response
