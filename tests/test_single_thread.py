import os
from unittest import TestCase

import sharedshell


class SingleThreadTestCase(TestCase):

    def test_echo_1(self):

        with sharedshell.SharedShell() as shell:

            ret = shell.run('echo 1')

            self.assertEqual(ret.stdout, '1' + os.linesep)
            self.assertEqual(ret.stderr, '')

    def test_echo_1_and_2(self):

        with sharedshell.SharedShell() as shell:

            ret_1 = shell.run('echo 1')
            ret_2 = shell.run('echo 2')

            self.assertEqual(ret_1.stdout, '1' + os.linesep)
            self.assertEqual(ret_1.stderr, '')

            self.assertEqual(ret_2.stdout, '2' + os.linesep)
            self.assertEqual(ret_2.stderr, '')

    def test_error_str(self):

        with sharedshell.SharedShell() as shell:

            ret = shell.run('>&2 echo ERROR')

            self.assertEqual(ret.stdout, '')
            self.assertEqual(ret.stderr, 'ERROR\n')

    def test_error_to_stdout(self):

        with sharedshell.SharedShell() as shell:

            ret = shell.run('>&2 echo ERROR', stderr=sharedshell.STDOUT)

            self.assertEqual(ret.stdout, '\nERROR\n')
            self.assertFalse(hasattr(ret, 'stderr'))
