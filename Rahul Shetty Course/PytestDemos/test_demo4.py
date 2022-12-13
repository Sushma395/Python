import pytest

from PytestDemos.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    # since dataLoad needs to be returned, it should be passed in method argument
    def test_editProfile(self, dataLoad):
        print(dataLoad)


# explained after demo 6 using logging baseclass

@pytest.mark.usefixtures("dataLoad")
class TestExample3(BaseClass):

    # since dataLoad needs to be returned, it should be passed in method argument
    def test_editProfile2(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[1])
