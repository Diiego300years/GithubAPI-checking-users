#here is nothing special, just for me


import json
import requests
#Proxy robić
#socket.io do robienia czatów
#testy regresyjne
# # Directly from dictionary
# with open('json_data.json', 'w') as outfile:
#     json.dump(json_string, outfile)
#
# # Using a JSON string
# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)


def check():
    list = []
    for i in my_projects:
        list.append(i['name'])
    return list

token = 'token'
username = "KentBeck"
repo = "TestDesiderata"
query_url = f"https://api.github.com/users/{username}/repos"
params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)

my_projects = r.json()



####################################
def something():
    dict = {}
    my_projects2 = []
    for i in check():

        headers2 = {'Authorization': f'token {token}',
                    "accetp": "application/vnd.github.v3+json",
                    "anon": "0"}
        query_url2 = f"https://api.github.com/repos/{username}/{i}/contributors"
        params2 = {
            "state": "open",

        }

        r2 = requests.get(query_url2, headers=headers2, params=params2)
        r2.raise_for_status()  # raises exception when not a 2xx response
        if r2.status_code != 204:
            my_projects2.append(r2.json())
            #tu zwraca mi dobrze, ale co dalej? Nie mogę tego wyciągnąć

    return my_projects2
#('GET /repos/{owner}/{repo}/contributors',
def answer():
    list = []
    for i in something():
        list.append(i[-1]['contributions'])
    list[7] = 0
    list[8] = 0

    return list

            #jest kilka dict w jednej array i ostatni jest poprawny. Dostac sie do ostatniego i wyciągnąć z niego contributions
if __name__ == '__main__':
    print(answer())

