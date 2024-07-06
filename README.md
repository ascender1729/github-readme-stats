# GitHub README Stats

**Current Version: 0.1.1**

[![PyPI version](https://badge.fury.io/py/github-readme-stats.svg)](https://badge.fury.io/py/github-readme-stats)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Automatically update your GitHub README with your latest GitHub statistics.

## Features

- Fetch and display key GitHub user statistics
- Automatically update your README file
- Customizable stat display
- Easy to integrate with GitHub Actions for automatic updates

## Installation

```bash
pip install github-readme-stats
```

## Quick Start

1. Create a GitHub Personal Access Token with `repo` scope.
2. Add the following Python script to your project:

```python
from github_readme_stats import GitHubStats, ReadmeUpdater

github_token = "your_github_token_here"
github_username = "your_github_username"

stats = GitHubStats(github_token, github_username)
user_stats = stats.get_stats()

updater = ReadmeUpdater("path/to/your/README.md")
updater.update(user_stats)
```

3. Add a `<!-- GITHUB_STATS -->` placeholder in your README where you want the stats to appear.

## Changelog

### [0.1.1] - 2023-07-07
- Updated project description and README
- Minor bug fixes and improvements

### [0.1.0] - 2023-07-06
- Initial release
- Basic GitHub stats fetching and README updating functionality

## Roadmap

- Language statistics
- Contribution graph integration
- Customizable themes for stat display
- Organization-level statistics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [PyPI Package](https://pypi.org/project/github-readme-stats/)
- [GitHub Repository](https://github.com/ascender1729/github-readme-stats)

## Support

If you encounter any issues or have questions, please [file an issue](https://github.com/ascender1729/github-readme-stats/issues) on the GitHub repository.