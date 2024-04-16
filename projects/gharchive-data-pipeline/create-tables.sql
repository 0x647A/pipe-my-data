CREATE TABLE projects (
    projectID BIGINT PRIMARY KEY,
    projectName TEXT,
    uniqueStargazers INT,
    uniqueForks INT,
    issuesCount INT,
    pullRequestsCount INT
);

CREATE TABLE users (
    userID BIGINT PRIMARY KEY,
    userLogin TEXT,
    starredProjects INT,
    createdIssues INT,
    createdPullRequests INT
);
