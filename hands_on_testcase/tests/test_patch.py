import unittest

import requests

from hands_on_testcase.utils import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalender(unittest.TestCase):

    # patch as decorator
    @patch('hands_on_testcase.utils.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    # patch as context manager
    def test_get_holidays_timeout_1(self):
        with patch('hands_on_testcase.utils.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    # Patching objects attributes
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout_2(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

