"""Module for updating README with GitHub statistics."""

from typing import Dict
from .exceptions import ReadmeUpdateError

class ReadmeUpdater:
    """Class to update README with GitHub statistics."""

    def __init__(self, readme_path: str):
        """
        Initialize ReadmeUpdater.

        Args:
            readme_path (str): Path to the README file.
        """
        self.readme_path = readme_path

    def update(self, stats: Dict[str, int]) -> None:
        """
        Update README with GitHub statistics.

        Args:
            stats (Dict[str, int]): Dictionary containing user statistics.

        Raises:
            ReadmeUpdateError: If there's an error updating the README file.
        """
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            stats_text = f"""
Joined GitHub {stats['ACCOUNT_AGE']} years ago. Since then, I've pushed {stats['COMMITS']} commits, opened {stats['ISSUES']} issues, submitted {stats['PULL_REQUESTS']} pull requests, and received {stats['STARS']} stars across {stats['REPOSITORIES']} personal projects. Contributed to {stats['REPOSITORIES_CONTRIBUTED_TO']} public repositories.
"""
            
            updated_content = content.replace('<!-- GITHUB_STATS -->', stats_text)
            
            with open(self.readme_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
        except IOError as e:
            raise ReadmeUpdateError(f"Error updating README: {str(e)}") from e