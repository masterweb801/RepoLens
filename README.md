# RepoLens

RepoLens is a project that fetches and analyzes a GitHub user's programming skills based on the repositories they have. It tracks the languages used across all repositories, counts how often each language is used, and calculates how many repositories the user has.

## Features:
- Fetches all programming languages used by a GitHub user.
- Counts how many times each language is used.
- Displays the total number of repositories of the user.
- Outputs a breakdown of languages and their usage.

## Requirements:
- Python 3.6 or higher
- `requests` library for making HTTP requests.

## Installation:
1. Clone the repository:
    ```bash
    git clone <your-repository-url>
    ```

2. Navigate to the project folder:
    ```bash
    cd <your-project-folder>
    ```

3. Install the required dependencies:
    ```bash
    pip install requests
    ```

4. Set up a personal GitHub access token:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Create a new token with `repo` and `user` permissions.
   - Copy the generated token.

5. Create a file named `api.py` and paste your GitHub token in it:
    ```python
    # api.py
    GITHUB_ACCESS_TOKEN = "your_personal_access_token_here"
    ```

## Usage:

1. Run the Python script:
    ```bash
    python fetch_github.py
    ```

2. The program will ask for the GitHub username:
    ```bash
    Enter GitHub username: <username>
    ```

3. The script will output the total number of repositories and the breakdown of languages used across those repositories.

Example output:
```bash
Total Repositories: 12
Language Usage:
  Python: 5 times
  JavaScript: 4 times
  C++: 2 times
```

## How It Works:
- The script uses GitHub's GraphQL API to query all repositories of a user.
- It collects the languages used in each repository and counts how many times each language appears.
- The total number of repositories is also tracked.
