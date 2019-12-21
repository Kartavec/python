import requests

headers = {
    'Accept': 'Accept: application/vnd.github.v3+json',
    "User-Agent": "URL/Emacs Emacs/26.1 (X11; x86_64-pc-linux-gnu)"
}
params = {
    'type': 'owner'
}
main_link = "https://api.github.com"
list_repo_api = '/users/{}/repos'
git_user = 'shaunlebron'
list_repo_request = list_repo_api.format(git_user)

response = requests.request('GET', main_link + list_repo_request, headers=headers, params=params)

print('User', git_user, 'has', len(response.json()), 'repositories')

for rep in response.json():
    print('Repository \'{}\''.format(rep['name']), 'has url', rep['html_url'])

# second assignment
main_url_scheme = 'https://xkcd.com/{}/info.0.json'

with open('output.log', 'w') as out_file:
    for i in range(100, 200):
        response = requests.get(main_url_scheme.format(i))
        logstring = 'comic name: {}, transcript: {}\n'.format(response.json()['title'], response.json()['transcript'])
        print(logstring)
        out_file.write(logstring)
