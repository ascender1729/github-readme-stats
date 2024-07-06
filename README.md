# GitHub README Stats

A Python package to update your GitHub README with your latest stats.

## Installation

```
pip install github-readme-stats
```

## Usage

```python
from github_readme_stats import GitHubStats, ReadmeUpdater

# Initialize GitHubStats
stats = GitHubStats(github_token, username)

# Get stats
user_stats = stats.get_stats()

# Update README
updater = ReadmeUpdater('path/to/your/README.md')
updater.update(user_stats)
```

Make sure to include a `<!-- GITHUB_STATS -->` placeholder in your README where you want the stats to appear.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.