"""
JiraRequests.
"""

import requests
import Jira.config as conf
import Jira.Tests.API.JiraRequests.endpoints as endpoints


def get_issue_by_id(key, fields='*all'):
    if fields != '*all':
        response = requests.get(conf.SETTINGS['api_base_url'] +
                                endpoints.issue_endpoint + '/' + key + '?fields=' + fields,
                                auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    else:
        response = requests.get(conf.SETTINGS['api_base_url'] + endpoints.issue_endpoint + '/' + key,
                                auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code, response.json()


def create_issue(issue):
    response = requests.post(conf.SETTINGS['api_base_url'] + endpoints.issue_endpoint, json=issue,
                             auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code, response.json()


def create_issue_bulk(issue):
    response = requests.post(conf.SETTINGS['api_base_url'] + endpoints.issue_endpoint + '/bulk', json=issue,
                             auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code, response.json()


def delete_issue(key):
    response = requests.delete(conf.SETTINGS['api_base_url'] + endpoints.issue_endpoint + '/' + key,
                               auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code


def update_issue(key, issue):
    response = requests.put(conf.SETTINGS['api_base_url'] + endpoints.issue_endpoint + '/' + key, json=issue,
                            auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code


def search_issue(criteria):
    response = requests.post(conf.SETTINGS['api_base_url'] + endpoints.search_endpoint, json=criteria,
                             auth=(conf.SETTINGS['login'], conf.SETTINGS['password']))
    return response.status_code, response.json()
