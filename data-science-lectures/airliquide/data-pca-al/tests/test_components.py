from nbresult import ChallengeResultTestCase


class TestComponents(ChallengeResultTestCase):
    def test_minimal_pc(self):
        self.assertEqual(self.result.n_components, 1)
