import unittest
from llm_multi_model_workshop.service import health_check_service


class TestHealthCheckService(unittest.TestCase):
    def test_health_check(self):
        expected = ("", 200)
        actual = health_check_service.health_check()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
