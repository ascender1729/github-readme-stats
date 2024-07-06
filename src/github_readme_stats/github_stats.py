"""Module for fetching GitHub user statistics."""

from datetime import datetime
from typing import Dict
from github import Github
from github.GithubException import GithubException
from .exceptions import APIError

class GitHubStats:
    """Class to fetch GitHub user statistics."""

    def __init__(self, token: str, username: str):
        """
        Initialize GitHubStats.

        Args:
            token (str): GitHub API token.
            username (str): GitHub username.
        """
        self.g = Github(token)
        self.username = username

    def get_stats(self) -> Dict[str, int]:
        """
        Fetch GitHub statistics for the user.

        Returns:
            Dict[str, int]: Dictionary containing user statistics.

        Raises:
            APIError: If there's an error fetching data from GitHub API.
        """
        try:
            user = self.g.get_user(self.username)
            account_age = (datetime.now() - user.created_at).days // 365
            repos = list(user.get_repos())
            
            commits = sum(repo.get_commits().totalCount for repo in repos if not repo.fork)
            issues = sum(repo.get_issues().totalCount for repo in repos if not repo.fork)
            prs = sum(repo.get_pulls().totalCount for repo in repos if not repo.fork)
            stars = sum(repo.stargazers_count for repo in repos if not repo.fork)
            personal_repos = len([repo for repo in repos if not repo.fork])
            
            contributed_repos = set()
            for event in user.get_public_events():
                if event.type == 'PullRequestEvent':
                    contributed_repos.add(event.repo.name)
            
            return {
                'ACCOUNT_AGE': account_age,
                'COMMITS': commits,
                'ISSUES': issues,
                'PULL_REQUESTS': prs,
                'STARS': stars,
                'REPOSITORIES': personal_repos,
                'REPOSITORIES_CONTRIBUTED_TO': len(contributed_repos)
            }
        except GithubException as e:
            raise APIError(f"Error fetching GitHub stats: {str(e)}") from e