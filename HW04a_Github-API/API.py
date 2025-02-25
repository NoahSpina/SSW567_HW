import requests
import json
from unittest.mock import patch, Mock
import unittest

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


# Unit tests using unittest and patching of requests.get
class TestGetUserRepoCommits(unittest.TestCase):
    @patch('requests.get')
    def test_successful_response(self, mock_get):
        # Fake user_id to test
        user_id = "testuser"

        # Fake repository list with two repos.
        fake_repos = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        # Now we can do a mock test to simulate github
        fake_repo_response = Mock()
        fake_repo_response.status_code = 200
        fake_repo_response.json.return_value = fake_repos

        # Fake commit responses: repo1 has 2 commits, repo2 has 1 commit.
        fake_commit_response_repo1 = Mock()
        fake_commit_response_repo1.status_code = 200
        fake_commit_response_repo1.json.return_value = [{"sha": "c1"}, {"sha": "c2"}]

        fake_commit_response_repo2 = Mock()
        fake_commit_response_repo2.status_code = 200
        fake_commit_response_repo2.json.return_value = [{"sha": "c3"}]

        # The first call to requests.get is for repos,
        # then one for each commit URL.
        mock_get.side_effect = [
            fake_repo_response,         # for repos call
            fake_commit_response_repo1,   # for repo1 commits
            fake_commit_response_repo2    # for repo2 commits
        ]

        result = get_user_repo_commits(user_id)
        expected = [
            "Repo: repo1 Number of commits: 2",
            "Repo: repo2 Number of commits: 1"
        ]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_error_on_repos(self, mock_get):
        # Simulate an error when fetching repositories (e.g., user not found)
        user_id = "testuser"
        fake_repo_response = Mock()
        fake_repo_response.status_code = 404
        mock_get.return_value = fake_repo_response

        result = get_user_repo_commits(user_id)
        self.assertEqual(result, [])

    @patch('requests.get')
    def test_error_on_commits(self, mock_get):
        # Simulate one repository's commits failing to fetch.
        user_id = "testuser"
        fake_repos = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        fake_repo_response = Mock()
        fake_repo_response.status_code = 200
        fake_repo_response.json.return_value = fake_repos

        # For repo1, error test (status code 404).
        fake_commit_response_repo1 = Mock()
        fake_commit_response_repo1.status_code = 404

        # For repo2, successful commit retrieval test.
        fake_commit_response_repo2 = Mock()
        fake_commit_response_repo2.status_code = 200
        fake_commit_response_repo2.json.return_value = [{"sha": "c1"}]

        mock_get.side_effect = [
            fake_repo_response,         # repos API call
            fake_commit_response_repo1,   # repo1 commits (error)
            fake_commit_response_repo2    # repo2 commits (success)
        ]

        result = get_user_repo_commits(user_id)
        # repo1 is skipped (API returned an error)
        expected = ["Repo: repo2 Number of commits: 1"]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_invalid_json_in_repos(self, mock_get):
        # JSON decoding error test.
        user_id = "testuser"
        fake_repo_response = Mock()
        fake_repo_response.status_code = 200
        fake_repo_response.json.side_effect = json.JSONDecodeError("Expecting value", "", 0)

        mock_get.return_value = fake_repo_response

        result = get_user_repo_commits(user_id)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()