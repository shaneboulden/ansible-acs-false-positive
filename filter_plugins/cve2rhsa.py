#!/usr/bin/python

import requests
import sys

class FilterModule(object):
    ''' CVE to RHSA filter '''

    def filters(self):
        return {
            'cve2rhsa': self.cve2rhsa
        }

    def get_data(query):
        PROXIES = {}
        full_query = API_HOST + query
        r = requests.get(full_query, proxies=PROXIES)

        if r.status_code != 200:
            print('ERROR: Invalid request; returned {} for the following '
                'query:\n{}'.format(r.status_code, full_query))
            sys.exit(1)

        if not r.json():
            print('No data returned with the following query:')
            print(full_query)
            sys.exit(0)

        return r.json()

    def cve2rhsa(self, cve):
        API_HOST = 'https://access.redhat.com/hydra/rest/securitydata'
        
        endpoint = '/csaf.json'
        params = "cve="+cve

        data = self.get_data(endpoint + '?' + params)
        rhsas = []
        for rhsa in data:
            rhsas.append(rhsa["RHSA"])

        return rhsas

