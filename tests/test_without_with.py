import os
from unittest import TestCase

import sharedshell


class WithoutWithTestCase(TestCase):

    def test_echo_1(self):

        shell = sharedshell.SharedShell()

        ret = shell.run('echo 1')

        self.assertEqual(ret.stdout, '1' + os.linesep)
        self.assertEqual(ret.stderr, '')
