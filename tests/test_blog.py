import unittest

from app.models import Posts


class TestModelPost(unittest.TestCase):
    def SetUp(self):
        self.new_post = Posts('Technology', 'Tech is the future', 0,0,0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Posts))