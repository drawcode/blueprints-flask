import git 

git_dir = '[dir]'

print git_dir

g = git.cmd.Git(git_dir)
print g.pull()