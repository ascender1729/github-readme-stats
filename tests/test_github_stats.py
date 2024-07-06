"""Unit tests for GitHub README Stats package."""

import unittest
from unittest.mock import patch, MagicMock
from github_readme_stats import GitHubStats, ReadmeUpdater, APIError, ReadmeUpdateError

class TestGitHubStats(unittest.TestCase):
    """Test cases for GitHubStats class."""

    @patch('github_readme_stats.github_stats.Github')
    def test_get_stats(self, mock_github):
        # Setup mock
        mock_user = MagicMock()
        mock_user.created_at.return_value = '2020-01-01'
        mock_user.get_repos.return_value = []
        mock_user.get_public_events.return_value = []
        mock_github.return_value.get_user.return_value = mock_user

        # Test
        stats = GitHubStats('fake_token', 'fake_username').get_stats()

        # Assert
        self.assertIsInstance(stats, dict)
        self.assertIn('ACCOUNT_AGE', stats)
        self.assertIn('COMMITS', stats)
        self.assertIn('ISSUES', stats)
        self.assertIn('PULL_REQUESTS', stats)
        self.assertIn('STARS', stats)
        self.assertIn('REPOSITORIES', stats)
        self.assertIn('REPOSITORIES_CONTRIBUTED_TO', stats)

class TestReadmeUpdater(unittest.TestCase):
    """Test cases for ReadmeUpdater class."""

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='<!-- GITHUB_STATS -->')
    def test_update(self, mock_open):
        stats = {
            'ACCOUNT_AGE': 1,
            'COMMITS': 100,
            'ISSUES': 10,
            'PULL_REQUESTS': 20,
            'STARS': 50,
            'REPOSITORIES': 5,
            'REPOSITORIES_CONTRIBUTED_TO': 3
        }

        updater = ReadmeUpdater('fake_path')
        updater.update(stats)

        mock_open.assert_called_with('fake_path', 'w', encoding='utf-8')
        handle = mock_open()
        handle.write.assert_called_once()
        written_content = handle.write.call_args[0][0]
        self.assertIn('1 years ago', written_content)
        self.assertIn('100 commits', written_content)

if __name__ == '__main__':
    unittest.main()