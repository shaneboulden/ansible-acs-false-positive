#!/usr/bin/python

import requests
import sys

class FilterModule(object):
    ''' CVE to RHSA filter '''

    def filters(self):
        return {
            'cve2rhsa': self.cve2rhsa
        }

    def get_data(self,query):
        PROXIES = {}
        API_HOST = 'https://access.redhat.com/hydra/rest/securitydata'
        full_query = API_HOST + query
        r = requests.get(full_query, proxies=PROXIES)

        if r.status_code != 200:
            print('ERROR: Invalid request; returned {} for the following '
                'query:\n{}'.format(r.status_code, full_query))
            sys.exit(1)

        return r.json()

    def cve2rhsa(self, cves):
        rhsas_and_cves = []
        endpoint = '/csaf.json'

        for cve in cves:
            params = "cve="+cve
            data = self.get_data(endpoint + '?' + params)

            if data:
                for csaf in data:
                    rhsas_and_cves.append(csaf["RHSA"])

            rhsas_and_cves.append(cve)

        return rhsas_and_cves

