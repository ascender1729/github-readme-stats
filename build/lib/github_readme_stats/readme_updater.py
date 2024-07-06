from .exceptions import ReadmeUpdateError

class ReadmeUpdater:
    def __init__(self, readme_path: str):
        self.readme_path = readme_path

    def update(self, stats: dict) -> None:
        try:
            with open(self.readme_path, 'r') as file:
                content = file.read()
            
            stats_text = f"""
Joined GitHub {stats['ACCOUNT_AGE']} years ago. Since then, I've pushed {stats['COMMITS']} commits, opened {stats['ISSUES']} issues, submitted {stats['PULL_REQUESTS']} pull requests, and received {stats['STARS']} stars across {stats['REPOSITORIES']} personal projects. Contributed to {stats['REPOSITORIES_CONTRIBUTED_TO']} public repositories.
"""
            
            updated_content = content.replace('<!-- GITHUB_STATS -->', stats_text)
            
            with open(self.readme_path, 'w') as file:
                file.write(updated_content)
        except IOError as e:
            raise ReadmeUpdateError(f"Error updating README: {str(e)}") from e