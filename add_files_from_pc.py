import os
import requests
import base64

# Your GitHub personal access token
# If dont have token then create from Personal access tokens (classic) -https://github.com/settings/tokens
access_token = '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'

# The owner of the repository (your GitHub username or organization)
owner = 'nitikshh'
repo_name = input("Repo name : ")

def add_file_to_repository(file_path, file_content):
    url = f'https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        payload = {'message': 'Update existing file', 'content': base64.b64encode(file_content.encode()).decode(), 'sha': response.json()['sha']}
        response = requests.put(url, headers=headers, json=payload)
    elif response.status_code == 404:
        payload = {'message': 'Create a new file', 'content': base64.b64encode(file_content.encode()).decode()}
        response = requests.put(url, headers=headers, json=payload)
    return response.status_code == 201

def main():
    while True:
        file_path = input("File Path (or 'exit' to quit): ")
        if 'exit' in file_path:
            print('Exiting')
            break
        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            continue
        with open(file_path, 'r') as file:
            file_content = file.read()
        if add_file_to_repository(os.path.basename(file_path), file_content):
            print(f'File added to "{repo_name}" successfully.')
            print(f"path - {file_path}")
        else:
            print(f'Failed to add the file to "{repo_name}".')

if __name__ == '__main__':
    main()