# git-get

## install

    sudo curl -L "https://raw.githubusercontent.com/d10xa/git-get/master/git_get.py" -o /usr/local/bin/git-get
    sudo chmod +x /usr/local/bin/git-get

## usage examples
    
    git get d10xa/git-get
    git get https://github.com/d10xa/git-get
    git get https://github.com/d10xa/git-get.git
    # Cloning into '~/github.com/d10xa/git-get'...
    
    git get https://bitbucket.org/user/repo.git
    # Cloning into '~/bitbucket.org/user/repo'...
    
    git get https://gitlab.com/gitlab-org/release/tasks
    # Cloning into '~/gitlab.com/gitlab-org/release/tasks'...
    
    git get https://try.gogs.io/d10xa/git-get
    # Cloning into '~/try.gogs.io/d10xa/git-get'...

## custom git path

    export GIT_GET_PATH="$HOME/projects"

