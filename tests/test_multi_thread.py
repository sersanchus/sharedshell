import os
import threading
from unittest import TestCase

from sharedshell import SharedShell


class MultiThreadTestCase(TestCase):

    def test_echo_1_on_secondary_thread(self):

        def _worker():

            shell = SharedShell()

            ret = shell.run('echo 1')

            self.assertEqual(ret.stdout, '1' + os.linesep)
            self.assertEqual(ret.stderr, '')

        t = threading.Thread(target=_worker)
        t.start()
        t.join()
