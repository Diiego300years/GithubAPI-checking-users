import requests
from prettytable import PrettyTable



class GithubAPI:
    def __init__(self, token, name):
        self.token = token
        self.name = name

    def check(self):
        list = []
        query_url = f"https://api.github.com/users/{self.name}/repos"
        params = {
            "state": "open",
        }
        headers = {'Authorization': f'token {self.token}'}
        r = requests.get(query_url, headers=headers, params=params)

        my_projects = r.json()

        for i in my_projects:
            list.append(i['name'])
        return list

    ####################################
    def something(self):
        my_projects2 = []

        for i in self.check():

            headers2 = {'Authorization': f'token {self.token}',
                        "accetp": "application/vnd.github.v3+json",
                        }
            query_url2 = f"https://api.github.com/repos/{self.name}/{i}/contributors"
            params2 = {
                "state": "open",

            }

            r2 = requests.get(query_url2, headers=headers2, params=params2)
            r2.raise_for_status()  # raises exception when not a 2xx response
            if r2.status_code != 204:
                my_projects2.append(r2.json())
            else:
                my_projects2.append(0)

        return my_projects2

    def answer(self):
        list = []
        for i in self.something():
            # print(i)
            if i != 0:
                list.append(i[-1]['contributions'])
            else:
                list.append(0)

        return list

    def request(self):
        headers = {'Authorization': f'token {self.token}'}
        query_url = f"https://api.github.com/users/{self.name}/repos"
        params = {
            "state": "open",
        }
        r = requests.get(query_url, headers=headers, params=params)
        my_projects = r.json()

        x = PrettyTable()
        for project, v in zip(my_projects, self.answer()):
            x.add_rows([[project['name'], project['size'], v, "---" if v == 0 else project["default_branch"], "---" if v == 0 else project['permissions']['admin']]])
            x.field_names = ["Name", "Size", "Contributors Count", "Branch", "Is Protected"]

        return x



token = 'Yours token'
username = "f.e. DominikWawak- it's my friend"

gh = GithubAPI(token, username)
print(gh.request())