"""
    SoftLayer.tests.CLI.modules.email_tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for the user cli command
"""
from SoftLayer import testing


class EmailCLITests(testing.TestCase):

    def test_detail(self):
        result = self.run_command(['email', 'list'])
        self.assert_no_fail(result)
        self.assert_called_with('SoftLayer_Account', 'getNetworkMessageDeliveryAccounts')
