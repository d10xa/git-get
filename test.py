import unittest

from git_get import parse_git_url, GitUrl


class Tests(unittest.TestCase):

    def test_parse_git_url(self):
        self.assertEqual(
            parse_git_url('https://github.com/github/hub.git'),
            GitUrl('github.com', None, 'github', 'hub', 'https://github.com/github/hub.git')
        )
        self.assertEqual(
            parse_git_url('https://gitlab.com/gitlab-org/release/tasks'),
            GitUrl('gitlab.com', "gitlab-org", 'release', 'tasks', 'https://gitlab.com/gitlab-org/release/tasks.git')
        )
        self.assertEqual(
            parse_git_url('https://github.com/github/hub'),
            GitUrl('github.com', None, 'github', 'hub', 'https://github.com/github/hub.git')
        )
        self.assertEqual(
            parse_git_url('https://bitbucket.org/user/repo'),
            GitUrl('bitbucket.org', None, 'user', 'repo', 'https://bitbucket.org/user/repo.git')
        )
        self.assertEqual(
            parse_git_url('git@bitbucket.org:user/repo.git'),
            GitUrl('bitbucket.org', None, 'user', 'repo', 'git@bitbucket.org:user/repo.git')
        )
        self.assertEqual(
            parse_git_url('user/repo'),
            GitUrl('github.com', None, 'user', 'repo', 'https://github.com/user/repo.git')
        )


if __name__ == '__main__':
    unittest.main()
