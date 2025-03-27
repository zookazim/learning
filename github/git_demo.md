# Git Demo


## 1. Clone Repo Locally (using VS Code)

### 2.1 Open VS Code and Clone Repo

<br>

![GitHub Clone Repo in VS Code](images/git_clone_repo_vs_code.png)


<br>


![GitHub Clone Repo in VS Code](images/git_clone_repo_vs_code_2.png)

<br>

You may be prompted to login to GitHub if you are not already logged in. When successfully logged in you will be presented with a list of repos to select from



## 2 Create a branch on remote repo (GitHub web page)

"New Branch" button


### 2.2 Check the branch is created from GitBash

```
$ git fetch
From https://github.com/Mental-Health-Commission/Synapse-Analytics-workspace
 * [new branch]        daves_test -> origin/daves_test
```

### 3.3 Create the Branch Locally

```
$ git branch --all
* daves_test_main
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/b3_wasms/coroners_office
  remotes/origin/b3_wasms/merge_suspected_cases
  remotes/origin/b3_wasms/project_b
  remotes/origin/c2_rmhs/project
  remotes/origin/c3_aodmds/c3_aodmds_notebook_updates
  remotes/origin/c3_aodmds/c3_aodmds_validation_rules_test
  remotes/origin/common/project
  remotes/origin/d1_mns/d1_mns_validation_v2
  remotes/origin/d1_mns/project
  remotes/origin/d2_bedstate/parameters_fixes
  remotes/origin/d6_hmdc/initial_setup
  remotes/origin/daves_test
  remotes/origin/daves_test_main
  remotes/origin/main
  remotes/origin/workspace_publ_prod/deployment_changes
  remotes/origin/workspace_publish
  remotes/origin/workspace_publish_prod

```

### 3.4 Create the Branch Locally

Use the git checkout command to create the branch and track the remote branch.

```
$ git checkout --track origin/daves_test
branch 'daves_test' set up to track 'origin/daves_test'.
Switched to a new branch 'daves_test'
```

Check that the branch has now been created and is in the list of local branches

```
$ git branch --all
* daves_test
  daves_test_main
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/b3_wasms/coroners_office
  remotes/origin/b3_wasms/merge_suspected_cases
  remotes/origin/b3_wasms/project_b
  remotes/origin/c2_rmhs/project
  remotes/origin/c3_aodmds/c3_aodmds_notebook_updates
  remotes/origin/c3_aodmds/c3_aodmds_validation_rules_test
  remotes/origin/common/project
  remotes/origin/d1_mns/d1_mns_validation_v2
  remotes/origin/d1_mns/project
  remotes/origin/d2_bedstate/parameters_fixes
  remotes/origin/d6_hmdc/initial_setup
  remotes/origin/daves_test
  remotes/origin/daves_test_main
  remotes/origin/main
  remotes/origin/workspace_publ_prod/deployment_changes
  remotes/origin/workspace_publish
  remotes/origin/workspace_publish_prod
```

## 2. Synapse Example Create a Branch

### 2.1 Create a branch on remote repo (GitHub web page)

"New Branch" button


### 2.2 Check the branch is created from GitBash

```
$ git fetch
From https://github.com/Mental-Health-Commission/Synapse-Analytics-workspace
 * [new branch]        daves_test -> origin/daves_test
```

### 2.3 Create the Branch Locally

```
$ git branch --all
* daves_test_main
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/b3_wasms/coroners_office
  remotes/origin/b3_wasms/merge_suspected_cases
  remotes/origin/b3_wasms/project_b
  remotes/origin/c2_rmhs/project
  remotes/origin/c3_aodmds/c3_aodmds_notebook_updates
  remotes/origin/c3_aodmds/c3_aodmds_validation_rules_test
  remotes/origin/common/project
  remotes/origin/d1_mns/d1_mns_validation_v2
  remotes/origin/d1_mns/project
  remotes/origin/d2_bedstate/parameters_fixes
  remotes/origin/d6_hmdc/initial_setup
  remotes/origin/daves_test
  remotes/origin/daves_test_main
  remotes/origin/main
  remotes/origin/workspace_publ_prod/deployment_changes
  remotes/origin/workspace_publish
  remotes/origin/workspace_publish_prod

```

### 2.4 Create the Branch Locally

Use the git checkout command to create the branch and track the remote branch.

```
$ git checkout --track origin/daves_test
branch 'daves_test' set up to track 'origin/daves_test'.
Switched to a new branch 'daves_test'
```

Check that the branch has now been created and is in the list of local branches

```
$ git branch --all
* daves_test
  daves_test_main
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/b3_wasms/coroners_office
  remotes/origin/b3_wasms/merge_suspected_cases
  remotes/origin/b3_wasms/project_b
  remotes/origin/c2_rmhs/project
  remotes/origin/c3_aodmds/c3_aodmds_notebook_updates
  remotes/origin/c3_aodmds/c3_aodmds_validation_rules_test
  remotes/origin/common/project
  remotes/origin/d1_mns/d1_mns_validation_v2
  remotes/origin/d1_mns/project
  remotes/origin/d2_bedstate/parameters_fixes
  remotes/origin/d6_hmdc/initial_setup
  remotes/origin/daves_test
  remotes/origin/daves_test_main
  remotes/origin/main
  remotes/origin/workspace_publ_prod/deployment_changes
  remotes/origin/workspace_publish
  remotes/origin/workspace_publish_prod
```