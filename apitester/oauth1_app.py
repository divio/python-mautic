# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from pprint import pformat

from flask import Flask, request, redirect, session, url_for, jsonify
from requests_oauthlib import OAuth1Session


app = Flask(__name__)

client_id = '205zi4jn0x1cw44cksw8g0wws44o8co4wsssg8wookgkgkg4ow'
client_secret = 'mqeis2ypomoso0sc4o84gc80k8k8occ8w00oc808o8wcwoc0w'

redirect_uri = 'http://localhost:8000/callback'


base_url = 'https://antsyferov.mautic.net/'
access_token_url = base_url + 'oauth/v1/access_token'
request_token_url = base_url + 'oauth/v1/request_token'
authorization_base_url = base_url + 'oauth/v1/authorize'


api_base_url = base_url + 'api/'
contacts_url = api_base_url + 'contacts'

extra = {
    'client_id': client_id,
    'client_secret': client_secret
}


@app.route("/")
def index():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider using an URL with a few key OAuth parameters.
    """
    mautic = OAuth1Session(client_id, client_secret=client_secret, callback_uri=redirect_uri)
    mautic.fetch_request_token(request_token_url)
    authorization_url = mautic.authorization_url(authorization_base_url, oauth_callback=redirect_uri)
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.
@app.route("/callback", methods=['GET'])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    mautic = OAuth1Session(client_id, client_secret=client_secret, callback_uri=redirect_uri,
                           signature_type='auth_header')
    mautic.parse_authorization_response(request.url)
    mautic.fetch_access_token(access_token_url)

    return redirect(url_for('.menu'))


@app.route("/menu", methods=["GET"])
def menu():
    """"""
    return """
    <h1>Congratulations, you have obtained an OAuth 2 token!</h1>
    <h2>What would you like to do next?</h2>
    <ul>
        <li><a href="/contacts"> Get contacts</a></li>
        <li><a href="/automatic_refresh"> Implicitly refresh the token</a></li>
        <li><a href="/manual_refresh"> Explicitly refresh the token</a></li>
        <li><a href="/validate"> Validate the token</a></li>
    </ul>

    <pre>
    %s
    </pre>
    """ % pformat(session['oauth_token'], indent=4)


@app.route("/contacts", methods=["GET"])
def contacts():
    """Fetching a protected resource using an OAuth 2 token.
    """
    mautic = OAuth1Session(client_id, token=session['oauth_token'])
    return jsonify(mautic.get(contacts_url).json())


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'A0Zr98j/3yXqewqweqqrqwr/,?RT'
    app.config['SERVER_NAME'] = 'localhost:8000'
    import os
    os.environ['DEBUG'] = '1'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['WERKZEUG_DEBUG_PIN'] = 'off'
    app.run(host='localhost', port=8000)
