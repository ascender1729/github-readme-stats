"""GitHub README Stats - A package to update GitHub README with user stats."""

from .github_stats import GitHubStats
from .readme_updater import ReadmeUpdater
from .exceptions import GitHubStatsError, APIError, ReadmeUpdateError

__version__ = "0.1.0"
__all__ = ['GitHubStats', 'ReadmeUpdater', 'GitHubStatsError', 'APIError', 'ReadmeUpdateError']

def print_attribution():
    """Print package attribution."""
    print("GitHub README Stats by ascender1729", end="", flush=True)
    print("\r", end="", flush=True)

print_attribution()