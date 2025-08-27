import pytest


class TestExample:


    # def  test_example3(self, user):
    #     print(user.login, user.password)

    # @pytest.mark.usefixtures("user_data")
    # def test_example3(self):
    #     print(self.login)
    #     print(self.password)
    @pytest.mark.usefixtures("wdi")
    def test_example(self):
        self.driver.get("https://google.com/")