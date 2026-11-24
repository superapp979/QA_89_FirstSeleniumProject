import pytest


@pytest.mark.skip(reason="Lesson outline: browser steps are still to be implemented.")
class TestLogin:
    @classmethod
    def setup_class(cls):
        # Open the browser and navigate to https://telranedu.pages.dev/home.
        pass

    def test_login_success(self):
        # Open the login form.
        # Clear the email and password fields and enter valid credentials.
        # Submit the form and check that the user is logged in.
        pass

    def test_login_wrong_email(self):
        # Open the login form.
        # Enter an invalid email and fill in the password.
        # Submit the form and check that login is rejected.
        pass

    def test_login_wrong_password(self):
        # Open the login form.
        # Enter a registered email and an incorrect password.
        # Submit the form and check that login is rejected.
        pass

    def test_login_unregistered_user(self):
        # Open the login form.
        # Enter an unregistered user's email and password.
        # Submit the form and check that login is rejected.
        pass

    @classmethod
    def teardown_class(cls):
        # Close the browser.
        pass
