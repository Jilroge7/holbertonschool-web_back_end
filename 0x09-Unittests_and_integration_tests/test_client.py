#!/usr/bin/env python3
"""
playing with parameterize, mock, patch
on client.py
"""
import unittest
from parameterized import parameterized
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
        org_url = 'https://api.github.com/orgs' + org_name
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
