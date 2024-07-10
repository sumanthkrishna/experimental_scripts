#pip install requests pandas


import requests
import pandas as pd
from datetime import datetime
from requests.auth import HTTPBasicAuth

# Define your Bitbucket credentials
USERNAME = 'your_username'
PASSWORD = 'your_password'

def get_branches(repo_url):
    """
    Get all branches from a Bitbucket repository.
    """
    branches_url = f"{repo_url}/refs/branches"
    response = requests.get(branches_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    
    if response.status_code != 200:
        raise Exception(f"Failed to get branches from {repo_url}. Status code: {response.status_code}")
    
    branches = response.json().get('values', [])
    return branches

def get_branch_details(repo_url, branch_name):
    """
    Get details of a specific branch from a Bitbucket repository.
    """
    branch_url = f"{repo_url}/refs/branches/{branch_name}"
    response = requests.get(branch_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    
    if response.status_code != 200:
        raise Exception(f"Failed to get details for branch {branch_name} from {repo_url}. Status code: {response.status_code}")
    
    branch_details = response.json()
    return branch_details

def generate_report(repositories):
    """
    Generate a report of branches by date, merge status, and last commit.
    """
    report_data = []

    for repo_url in repositories:
        branches = get_branches(repo_url)
        
        for branch in branches:
            branch_name = branch['name']
            branch_details = get_branch_details(repo_url, branch_name)
            last_commit_date = branch_details['target']['date']
            is_merged = branch_details.get('merge_commit', None) is not None
            
            report_data.append({
                'Repository': repo_url,
                'Branch': branch_name,
                'Last Commit Date': last_commit_date,
                'Merged': is_merged
            })
    
    # Create a DataFrame and save it as a CSV file
    df = pd.DataFrame(report_data)
    df.to_csv('branch_report.csv', index=False)
    print("Report generated successfully: branch_report.csv")

# List of Bitbucket repository URLs
repositories = [
    'https://api.bitbucket.org/2.0/repositories/your_workspace/your_repo1',
    'https://api.bitbucket.org/2.0/repositories/your_workspace/your_repo2',
    # Add more repositories as needed
]

generate_report(repositories)
