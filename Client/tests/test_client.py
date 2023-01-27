from unittest import TestCase

from clientUtils import isPlanValid
from tests.conftest import *


class TestClient(TestCase):
    def testPlanValid(self):
        inputs = ["this", "that", "small", "medium", "large"]
        expectedOut = [False, False, True, True, True]
        for index, inp in enumerate(inputs):
            self.assertEqual(isPlanValid(inp), expectedOut[index])
