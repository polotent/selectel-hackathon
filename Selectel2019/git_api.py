import requests
import re
import json


class GitProcessor:
    def __init__(self, repo_link):
        if repo_link[len(repo_link)-4:] == ".git":
            repo_link = repo_link[:len(repo_link)-4]
        self.repo_link = repo_link

    def get_history(self, num_of_commits=5):
        try:
            temp_arr = re.split(r'[/:]', self.repo_link)
            repo_name = temp_arr[len(temp_arr)-1]
            repo_owner = temp_arr[len(temp_arr)-2]

            response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits')
            commit_dict = dict()
            content = json.loads(response.content)
            for el in content:
                if el["commit"]["author"]["name"] not in commit_dict:
                    commit_dict[el["commit"]["author"]["name"]] = [
                        {
                            "time": el["commit"]["author"]["date"],
                            "message": el["commit"]["message"]
                        }
                    ]
                else:
                    commit_dict[el["commit"]["author"]["name"]].append(
                        {
                            "time": el["commit"]["author"]["date"],
                            "message": el["commit"]["message"]
                        }
                    )
            return commit_dict
        except Exception:
            return list()
