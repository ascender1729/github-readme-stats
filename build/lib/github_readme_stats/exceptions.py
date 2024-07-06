class GitHubStatsError(Exception):
    """Base exception for GitHub stats errors"""

class APIError(GitHubStatsError):
    """Raised when there's an error with the GitHub API"""

class ReadmeUpdateError(GitHubStatsError):
    """Raised when there's an error updating the README"""