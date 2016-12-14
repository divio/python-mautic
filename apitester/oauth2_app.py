# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from pprint import pformat
from time import time

from flask import Flask, request, redirect, session, url_for, jsonify
from requests_oauthlib import OAuth2Session

from python_mautic.utils import update_token_tempfile

app = Flask(__name__)

client_id = '1_31smsiab0jacsso4wkc0c0ss0440wgs40wowosccssoc40gock'
client_secret = '1wu2w2qj8r5wc8soowg0oo8cwk0c0gwg0s0cw0gckcoo0w4sgs'
redirect_uri = 'http://localhost:8000/callback'


base_url = 'https://antsyferov.mautic.net/'
authorization_base_url = base_url + 'oauth/v2/authorize'
token_url = base_url + 'oauth/v2/token'
refresh_url = token_url

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
    mautic = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = mautic.authorization_url(authorization_base_url, grant_type='authorization_code')

    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.
@app.route("/callback", methods=['GET'])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    mautic = OAuth2Session(client_id, redirect_uri=redirect_uri,
                           state=session['oauth_state'])
    token = mautic.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

    # We use the session as a simple DB for this example.
    session['oauth_token'] = token
    update_token_tempfile(token)

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
    mautic = OAuth2Session(client_id, token=session['oauth_token'])
    return jsonify(mautic.get(contacts_url).json())


@app.route("/automatic_refresh", methods=["GET"])
def automatic_refresh():
    """Refreshing an OAuth 2 token using a refresh token.
    """
    token = session['oauth_token']

    # We force an expiration by setting expired at in the past.
    # This will trigger an automatic refresh next time we interact with
    token['expires_at'] = time() - 10

    def token_updater(token):
        session['oauth_token'] = token

    mautic = OAuth2Session(client_id,
                           token=token,
                           auto_refresh_kwargs=extra,
                           auto_refresh_url=refresh_url,
                           token_updater=token_updater)

    # Trigger the automatic refresh
    return jsonify(session['oauth_token'])


@app.route("/manual_refresh", methods=["GET"])
def manual_refresh():
    """Refreshing an OAuth 2 token using a refresh token.
    """
    token = session['oauth_token']

    mautic = OAuth2Session(client_id, token=token)
    session['oauth_token'] = mautic.refresh_token(refresh_url, **extra)
    token = jsonify(session['oauth_token'])
    return token

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'A0Zr98j/3yXqewqweqqrqwr/,?RT'
    app.config['SERVER_NAME'] = 'localhost:8000'
    import os
    os.environ['DEBUG'] = '1'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['WERKZEUG_DEBUG_PIN'] = 'off'
    app.run(host='localhost', port=8000)
