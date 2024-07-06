# GitHub README Stats

A Python package to update your GitHub README with your latest stats.

## Installation

```bash
pip install github-readme-stats
```

## Usage

1. First, you need to create a GitHub Personal Access Token:
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Click "Generate new token"
   - Give it a name and select the `repo` scope
   - Copy the generated token

2. Use the package in your Python script:

```python
from github_readme_stats import GitHubStats, ReadmeUpdater

# Initialize GitHubStats with your GitHub token and username
github_token = "your_github_token_here"
github_username = "your_github_username"
stats = GitHubStats(github_token, github_username)

# Get stats
user_stats = stats.get_stats()

# Update README
readme_path = "path/to/your/README.md"
updater = ReadmeUpdater(readme_path)
updater.update(user_stats)
```

3. Make sure to include a `<!-- GITHUB_STATS -->` placeholder in your README where you want the stats to appear.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.