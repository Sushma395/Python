import pytest

'''
removed code and moved to conftest.py
@pytest.fixture()
def setup():
    print('First step to be executed')
    yield
    # teardown
    print('Last step to be executed')
'''


def test_fixtureProgram(setup):  # pass fixture method name as argument
    print('Execute steps in fixture demo method')


@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixtureDemo1(self):
        print('Execute steps in fixture demo1 method')

    def test_fixtureDemo2(self):
        print('Execute steps in fixture demo2 method')

    def test_fixtureDemo3(self):
        print('Execute steps in fixture demo3 method')
