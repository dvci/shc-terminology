import datetime as dt
import re
from os import environ

import requests
from dotenv import load_dotenv


class Icd11Fetcher:
    def __init__(self):
        load_dotenv()
        self.client_id = environ.get('ICD11_CLIENT')
        self.client_secret = environ.get('ICD11_CLIENT_SECRET')
        self.token = None
        self.expire_time = None

    def get_token(self):
        if self.token and dt.datetime.now() < self.expire_time:
            # the existing token is still valid so use it
            return self.token

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'icdapi_access',
            'grant_type': 'client_credentials'
        }
        r = requests.post('https://icdaccessmanagement.who.int/connect/token', data=payload)

        token_response = r.json()
        self.token = token_response['access_token']
        self.expire_time = dt.datetime.now() + dt.timedelta(seconds=token_response['expires_in'])

        return self.token

    def _get(self, uri):
        headers = {'Authorization': 'Bearer ' + self.get_token(),
                   'Accept': 'application/json',
                   'Accept-Language': 'en',
                   'API-Version': 'v2'}
        return requests.get(uri, headers=headers)

    @staticmethod
    def extract_release_from_mms_uri(uri):
        regex_pattern = r"http://id\.who\.int/icd/release/11/([^/]*)/mms"

        match = re.search(regex_pattern, uri)
        if match:
            extracted_value = match.group(1)
            return extracted_value
        else:
            raise Exception(f'No release found in {uri}.')

    @staticmethod
    def extract_entity_from_mms_uri(uri):
        regex_pattern = r"http://id\.who\.int/icd/release/11/[^/]*/mms/([0-9]+)"

        match = re.search(regex_pattern, uri)
        if match:
            extracted_value = match.group(1)
            return extracted_value
        else:
            raise Exception(f'No entity id found in {uri}.')

    def get_latest_release_for_entity(self, entity_id):
        uri = f'https://id.who.int/icd/release/11/mms/{entity_id}'
        r = self._get(uri).json()
        latest = r['latestRelease']
        return self.extract_release_from_mms_uri(latest)

    def get_mms_descendants_for_entity(self, entity_id, release):
        uri = f'https://id.who.int/icd/release/11/{release}/mms/{entity_id}?include=descendant'
        r = self._get(uri).json()

        # Get ICD-11 MMS codes for descendants
        out = {}
        for entity_uri in r['descendant']:
            r2 = self._get(entity_uri).json()
            out[r2['code']] = r2['title']['@value']
        return out

    @staticmethod
    def descendants_to_fsh(descendants):
        return "\n".join([f'* $icd11-mms#{k} "{v}"' for k, v in descendants.items()])
