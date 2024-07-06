# GitHub README Stats

**Current Version: 0.1.0**

[![PyPI version](https://badge.fury.io/py/github-readme-stats.svg)](https://badge.fury.io/py/github-readme-stats)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package to update your GitHub README with your latest stats.

## Installation

```bash
pip install github-readme-stats
```

## Usage

1. Create a GitHub Personal Access Token:
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

3. Include a `<!-- GITHUB_STATS -->` placeholder in your README where you want the stats to appear.

## Future Features (Roadmap for Version 0.2.0)

We're planning to add the following features in the next version:

1. Customizable stat display
2. Markdown formatting options
3. Language statistics
4. Contribution graph
5. Recent activity display
6. Badge generation for repository stats
7. Automatic scheduling for README updates
8. Theme support for stat display
9. Organization-level statistics
10. Contributor recognition feature

We welcome suggestions and contributions for these new features!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- PyPI: [https://pypi.org/project/github-readme-stats/](https://pypi.org/project/github-readme-stats/)
- GitHub: [https://github.com/ascender1729/github-readme-stats](https://github.com/ascender1729/github-readme-stats)

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.