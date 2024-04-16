import pandas as pd

def process_data_with_pandas(filename):

    df = pd.read_json(filename, lines=True)
    
    df['repo_id'] = df['repo'].apply(lambda x: x['id'])
    df['repo_name'] = df['repo'].apply(lambda x: x['name'])
    df['user_id'] = df['actor'].apply(lambda x: x['id'])
    df['user_login'] = df['actor'].apply(lambda x: x['login'])

    projects_agg = df.groupby('repo_id', as_index=False).agg(
        projectID=('repo_id', 'first'),
        projectName=('repo_name', 'first'),
        uniqueStargazers=('user_id', lambda x: x[df['type'] == 'WatchEvent'].nunique()),
        uniqueForks=('user_id', lambda x: x[df['type'] == 'ForkEvent'].nunique()),
        issuesCount=('type', lambda x: (x == 'IssuesEvent').sum()),
        pullRequestsCount=('type', lambda x: (x == 'PullRequestEvent').sum())
    )
    
    users_agg = df.groupby('user_id', as_index=False).agg(
        userID=('user_id', 'first'),
        userLogin=('user_login', 'first'),
        starredProjects=('repo_id', lambda x: x[df['type'] == 'WatchEvent'].nunique()),
        createdIssues=('type', lambda x: (x == 'IssuesEvent').sum()),
        createdPullRequests=('type', lambda x: (x == 'PullRequestEvent').sum())
    )
    
    return projects_agg, users_agg
