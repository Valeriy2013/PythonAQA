"""
JiraRequests tests.
"""

from Jira.Tests.API.DataProvider import json_data_provider
from Jira.Tests.API.JiraRequests import jira_requests
import pytest


@pytest.mark.api
class TestJiraRequests:

    def test_create_issue(self):
        # create an issue
        file = "issue_to_create.json"
        issue_to_create = json_data_provider.get_json_data(file)
        status_code, response = jira_requests.create_issue(issue_to_create)
        assert status_code == 201

        # get created issue and check fields
        new_key = response['key']
        get_status_code, get_response = jira_requests.get_issue_by_id(new_key, 'summary,description')
        assert get_status_code == 200
        assert get_response['fields']['summary'] == "Created via REST"
        assert get_response['fields']['description'] == "Creating of an issue using project keys and issue type names using the REST API"

        # delete created issue
        jira_requests.delete_issue(new_key)

    def test_delete_issue(self):
        # create issue for deletion
        file = "issue_to_create.json"
        issue_to_create = json_data_provider.get_json_data(file)
        status_code, response = jira_requests.create_issue(issue_to_create)

        # delete issue
        new_key = response['key']
        del_code = jira_requests.delete_issue(new_key)
        assert del_code == 204

        # check issue not exist after deletion
        get_status_code, get_response = jira_requests.get_issue_by_id(new_key, 'summary,description')
        assert get_status_code == 404

    def test_update_issue(self):
        # create issue for update
        file = "issue_to_create.json"
        issue_to_create = json_data_provider.get_json_data(file)
        status_code, response = jira_requests.create_issue(issue_to_create)

        # update issue
        new_key = response['key']
        file = "issue_to_update.json"
        issue_to_update = json_data_provider.get_json_data(file)
        upd_code = jira_requests.update_issue(new_key, issue_to_update)
        assert upd_code == 204

        # get updated issue and check fields
        get_status_code, get_response = jira_requests.get_issue_by_id(new_key, 'summary,description')
        assert get_status_code == 200
        assert get_response['fields']['summary'] == "Updated via REST"
        assert get_response['fields']['description'] == "Updated description"

        # delete updated issue
        jira_requests.delete_issue(new_key)

    def test_search_issue(self):
        # create issue for search using bulk create
        file = "issues_to_create_for_search.json"
        issues_to_create = json_data_provider.get_json_data(file)
        status_code, response = jira_requests.create_issue_bulk(issues_to_create)

        # retrieve created issues keys from response
        keys = []
        keys_length = len(response["issues"])
        for i in range(0, keys_length):
            keys.append(response["issues"][i]["key"])

        # search created issues
        file = "search_criteria.json"
        search_criteria = json_data_provider.get_json_data(file)
        search_status_code, search_response = jira_requests.search_issue(search_criteria)
        assert search_status_code == 200

        # delete created issues
        jira_requests.delete_issue(keys[0])
        jira_requests.delete_issue(keys[1])
