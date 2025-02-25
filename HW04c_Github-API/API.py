import requests
import json

def get_user_repo_commits(user_id):
    """
    Takes in a user_id and print their Github repos and # of commits of
    :param user_id: Github user id
    :return: void. Prints # of commits of repos for given user
    """
    results = []

    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        print(f"Error getting repositories for user \"{user_id}\"")
        return results

    # parse the data
    try:
        repos = repos_response.json()
    except json.JSONDecodeError:
        print(f"Error getting repositories for user \"{user_id}\"")
        return results


    # get commit count for each repo
    for repo in repos:
        repo_name = repo.get("name")
        if not repo_name:
            continue

        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            print(f"Error getting commits for repository \"{repo_name}\"")
            continue

        try:
            commits = commits_response.json()
        except json.JSONDecodeError:
            print(f"Error getting commits for repository \"{repo_name}\"")
            continue

        commit_count = len(commits)
        results.append(f"Repo: {repo_name} Number of commits: {commit_count}")

    return results
