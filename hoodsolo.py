from requests import Request, Session,ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import endpoints
# TO DO: use git encryption
class HoodSolo:

    auth_token = None
    oauth_token = None
    session = None

    def __init__(self):
        self.session = Session();

    def login(self, username, password):
        payload = {
            'client_id': 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS',
            'expires_in': 86400,
            'grant_type': 'password',
            'password': password,
            'scope': 'internal',
            'username': username,
            'mfa_code': 'none'
        }
        try:
            res = self.session.post(endpoints.login(), data=payload, timeout=15)
            res.raise_for_status()
            data = res.json()
            self.auth_token = data['access_token']
            self.session.headers['Authorization'] = 'Token ' + self.auth_token
            print(self.auth_token)
            print("Logged in")
            return data
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            raise(e)

    def logout(self):
        try:
            req = self.session.post(endpoints.logout(), timeout=15)
            req.raise_for_status()
        except (HTTPError) as e:
            raise e;

    def accountInfo(self):
        if (self.session.headers == None):
            print("Log in first")
            return
        res = self.session.post(endpoints.accounts(), timeout=15);
        res.raise_for_status()
        res = res.json()
        print(res)
        return res
