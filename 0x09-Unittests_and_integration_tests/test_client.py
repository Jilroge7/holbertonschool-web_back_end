#!/usr/bin/env python3
"""
playing with parameterize, mock, patch
on client.py
"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import requests
import json
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    class to test org
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'key': 'val'})
    def test_org(self, org_name, mock_get_json):
        """
        method for testing client.org
        """
        test_org = GithubOrgClient(org_name)
        org_url = 'https://api.github.com/orgs/' + org_name
        self.assertEqual(test_org.org, {'key': 'val'})
        mock_get_json.assert_called_once_with(org_url)

    def test_public_repos_url(self):
        """
        test for client._public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_github_org:
            mocked_github_org.return_value = {'repos_url': 'mock_url.com'}
            test_instance = GithubOrgClient('test_new_org')
            self.assertEqual(test_instance._public_repos_url, 'mock_url.com')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        method to test client.public_repos
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo_url:
            test_payload = {
                "login": "google",
                "id": 1342004,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                "gravatar_id": "",
                "url": "https://api.github.com/users/google",
                "repos_url": "https://api.github.com/users/google/repos"
            }
            test_instance = GithubOrgClient('test_org_name')
            mock_get_json.return_value = test_payload
            mock_repo_url.return_value = test_instance.org.get('repos_url')
            self.assertEqual(test_instance._public_repos_url,
                             "https://api.github.com/users/google/repos")
            mock_get_json.assert_called_once()
            mock_repo_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        test to measure functionality of client.has_license method
        """
        test_instance = GithubOrgClient('test_name')
        self.assertEqual(test_instance.has_license(repo, license_key),
                         expected)

    @parameterized_class([

    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """
        class for integration testing
        """
        @classmethod
        def setUpClass(cls):
            """
            setup class will mock the request from
            GithubOrgClient.public_repos
            ***starts the test***
            """
            cls.get_patcher = patch('requests.get')
            cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls):
            """
            teardown class to stop the patcher
            """
            cls.get_patcher.stop()

        def test_public_repo(self):
            """
            Incomplete test for client.public_repo
            """
            test_instance = GithubOrgClient('test_name')

        def test_public_repos_with_license(self):
            """
            Incomplete test for public_repos_with_license
            """
            test_instance = GithubOrgClient('test_name')
