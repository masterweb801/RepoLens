# RepoLens

RepoLens is a small Python command-line tool that analyzes a GitHub user's repositories and summarizes the programming languages used across them.

Enter a GitHub username and RepoLens queries GitHub's GraphQL API, counts repositories, and reports how many repositories use each detected language.

## Features

- Looks up repositories belonging to a GitHub user.
- Paginates through repository results rather than stopping at the first page.
- Collects the languages reported for each repository.
- Counts language appearances across repositories.
- Prints the total repository count and a language-usage summary in the terminal.

## Example output

```text
Enter GitHub username: octocat
Total Repositories: 12
Language Usage:
  Python: 5 times
  JavaScript: 4 times
  C++: 2 times
```

The values above are illustrative; actual results depend on the selected GitHub account.

## Requirements

- Python 3.6 or newer
- `requests`
- A GitHub personal access token configured locally

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/masterweb801/RepoLens.git
cd RepoLens
```

Install the dependency:

```bash
python -m pip install requests
```

Create a local file named `api.py` in the project directory:

```python
GITHUB_ACCESS_TOKEN = "YOUR_GITHUB_TOKEN"
```

Then run:

```bash
python main.py
```

When prompted, enter the GitHub username to analyze.

## Token safety

The current source imports `GITHUB_ACCESS_TOKEN` from `api.py`. Keep that file local and private:

- Never commit `api.py` or paste a real token into source code.
- Use a token with only the permissions required for the repositories you intend to inspect.
- For public repository statistics, avoid granting private-repository access unless you specifically need it.
- Revoke a token immediately if it is exposed.

## How it works

RepoLens sends a GraphQL request to `https://api.github.com/graphql`. It requests repository pages for the supplied username, reads each repository's language nodes, and uses Python's `Counter` to aggregate the results.

The current implementation counts a language once per repository when that language appears in the repository's returned language list. It is therefore a repository-usage count, not a measure of lines of code or language percentages.

## Limitations

- The current interface is terminal-based.
- It reports language occurrence by repository, not byte or line proportions.
- The result depends on the repositories and language metadata visible to the configured GitHub token.
- The project currently expects a local `api.py` file; do not run it until that file is configured.

## Project

Developed by **Logic Realm**.

- [Logic Realm](https://logicrealm.rf.gd/)
- [Source code](https://github.com/masterweb801/RepoLens)
