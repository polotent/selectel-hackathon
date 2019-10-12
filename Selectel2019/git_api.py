import requests
import re
import json


class GitProcessor:
    def get_history(repo_link, num_of_commits="inf", start_time=None, end_time=None):
        try:
            if repo_link[len(repo_link)-4:] == ".git":
                repo_link = repo_link[:len(repo_link)-4]

            temp_arr = re.split(r'[/:]', repo_link)
            repo_name = temp_arr[len(temp_arr)-1]
            repo_owner = temp_arr[len(temp_arr)-2]

            if start_time is None and end_time is None:
                response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits')
            else:
                start_time_parsed, end_time_parsed = 1, 2
                response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits?since={start_time_parsed}&until={end_time_parsed}')
            commit_dict = dict()
            content = json.loads(response.content)
            for el in content:
                if el["commit"]["author"]["date"] not in commit_dict:
                    commit_dict[el["commit"]["author"]["date"]] = [
                        {
                            "author": el["commit"]["author"]["name"],
                            "message": el["commit"]["message"]
                        }
                    ]
                else:
                    commit_dict[el["commit"]["author"]["date"]].append(
                        {
                            "author": el["commit"]["author"]["name"],
                            "message": el["commit"]["message"]
                        }
                    )
            commits = sorted(commit_dict.items())
            if num_of_commits == "inf":
                return commits
            else:
                return commits[:num_of_commits]
        except Exception:
            return list()
