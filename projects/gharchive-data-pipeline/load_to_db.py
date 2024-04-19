import psycopg2
from os import environ

PG_USER = environ["PG_USER"]
PG_PASS = environ["PG_PASS"]

def load_data_to_db(projects_agg, users_agg):

    conn = psycopg2.connect(
        dbname='daria', user=PG_USER, password=PG_PASS, host='127.0.0.1'
    )
    cur = conn.cursor()

    for _, row in projects_agg.iterrows():
        cur.execute(
            "INSERT INTO projects (projectID, projectName, uniqueStargazers, uniqueForks, issuesCount, pullRequestsCount) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (projectID) DO UPDATE SET projectName = EXCLUDED.projectName, uniqueStargazers = EXCLUDED.uniqueStargazers, uniqueForks = EXCLUDED.uniqueForks, issuesCount = EXCLUDED.issuesCount, pullRequestsCount = EXCLUDED.pullRequestsCount;",
            (row['projectID'], row['projectName'], row['uniqueStargazers'], row['uniqueForks'], row['issuesCount'], row['pullRequestsCount'])
        )

    for _, row in users_agg.iterrows():
        cur.execute(
            "INSERT INTO users (userID, userLogin, starredProjects, createdIssues, createdPullRequests) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (userID) DO UPDATE SET userLogin = EXCLUDED.userLogin, starredProjects = EXCLUDED.starredProjects, createdIssues = EXCLUDED.createdIssues, createdPullRequests = EXCLUDED.createdPullRequests;",
            (row['userID'], row['userLogin'], row['starredProjects'], row['createdIssues'], row['createdPullRequests'])
        )

    conn.commit()
    cur.close()
    conn.close()
