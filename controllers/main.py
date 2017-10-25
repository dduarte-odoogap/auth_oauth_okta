# -*- coding: utf-8 -*-
from odoo.addons.auth_oauth.controllers.main import OAuthLogin
from odoo.http import request


class OktaOAuthLogin(OAuthLogin):
    def list_providers(self):
        env = request.env
        providers = super(OktaOAuthLogin, self).list_providers()
        if providers:
            okta = env['auth.oauth.provider'].sudo().search([
                ('id', '=', env.ref('smart_shop_oauth.auth_oauth_provider_okta').id),
            ], limit=1)
            if okta:
                for provider in providers:
                    # Replace response_type token with code if Okta OAuth
                    if provider['auth_endpoint'] == okta[0].auth_endpoint:
                        provider['auth_link'] = provider['auth_link'].replace('response_type=token',
                                                                              'response_type=code')
        return providers
