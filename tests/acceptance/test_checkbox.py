import sys
import unittest

import pexpect
from readchar import key


@unittest.skipUnless(sys.platform.startswith("lin"), "Linux only")
class CheckTest(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox.py")
        self.sut.expect("History.*", timeout=1)

    def test_default_input(self):
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books'\]}.*", timeout=1)  # noqa

    def test_select_the_third(self):
        self.sut.send(key.DOWN)
        self.sut.send(key.DOWN)
        self.sut.send(key.SPACE)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science'\]}.*", timeout=1)  # noqa

    def test_select_one_more(self):
        self.sut.send(key.DOWN)
        self.sut.send(key.DOWN)
        self.sut.send(key.SPACE)
        self.sut.send(key.DOWN)
        self.sut.send(key.SPACE)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science', 'Nature'\]}.*", timeout=1)  # noqa

    def test_unselect(self):
        self.sut.send(key.SPACE)
        self.sut.send(key.SPACE)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Books', 'Computers'\]}.*", timeout=1)  # noqa

    def test_select_with_arrows(self):
        self.sut.send(key.DOWN)
        self.sut.send(key.DOWN)
        self.sut.send(key.RIGHT)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'Science'\]}.*", timeout=1)  # noqa

    def test_unselect_with_arrows(self):
        self.sut.send(key.DOWN)
        self.sut.send(key.LEFT)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers'\]}.*", timeout=1)  # noqa

    def test_select_last(self):
        for i in range(10):
            self.sut.send(key.DOWN)
        self.sut.send(key.SPACE)
        self.sut.send(key.ENTER)
        self.sut.expect(r"{'interests': \['Computers', 'Books', 'History'\]}.*", timeout=1)  # noqa


@unittest.skipUnless(sys.platform.startswith("lin"), "Linux only")
class CheckWithTaggedValuesTest(unittest.TestCase):
    def setUp(self):
        self.sut = pexpect.spawn("python examples/checkbox_tagged.py")
        self.sut.expect("History.*", timeout=1)

    def test_default_selection(self):
        self.sut.send(key.ENTER)
        self.sut.expect("{'interests': ", timeout=1)
