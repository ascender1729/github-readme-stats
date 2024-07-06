from .github_stats import GitHubStats
from .readme_updater import ReadmeUpdater
from .exceptions import GitHubStatsError, APIError, ReadmeUpdateError

__version__ = "0.1.0"

def print_attribution():
    print("Developed by ascender1729", end="", flush=True)
    print("\r", end="", flush=True)

print_attribution()