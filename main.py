import requests
from collections import Counter
from api import GITHUB_ACCESS_TOKEN

# GitHub GraphQL API URL
URL = "https://api.github.com/graphql"

# Headers with authentication
HEADERS = {
    "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Function to fetch all programming languages used by a GitHub user
def fetch_language_stats(username):
    language_list = []  # List to track all languages
    repo_count = 0  # Counter for total repositories
    has_next_page = True
    end_cursor = None

    while has_next_page:
        query = f"""
        {{
          user(login: "{username}") {{
            repositories(first: 100, after: {f'"{end_cursor}"' if end_cursor else 'null'}) {{
              pageInfo {{
                hasNextPage
                endCursor
              }}
              nodes {{
                languages(first: 10) {{
                  nodes {{
                    name
                  }}
                }}
              }}
            }}
          }}
        }}
        """
        response = requests.post(URL, json={"query": query}, headers=HEADERS)
        data = response.json()

        if "errors" in data:
            print("Error:", data["errors"])
            return {}, 0

        repo_data = data["data"]["user"]["repositories"]
        has_next_page = repo_data["pageInfo"]["hasNextPage"]
        end_cursor = repo_data["pageInfo"]["endCursor"]

        # Process repositories
        for repo in repo_data["nodes"]:
            repo_count += 1  # Count repositories
            for language in repo["languages"]["nodes"]:
                language_list.append(language["name"])  # Add language to list

    # Count occurrences of each language
    language_counts = dict(Counter(language_list))

    return language_counts, repo_count

# Example usage
if __name__ == "__main__":
    username = "octocat"  # Change this to test with different GitHub usernames
    language_counts, total_repos = fetch_language_stats(username)

    print(f"Total Repositories: {total_repos}")
    print("Language Usage:")
    for lang, count in language_counts.items():
        print(f"  {lang}: {count} times")
