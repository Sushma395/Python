# file/tests/methods should start with test_ or end with _test
# type pytest in terminal to run all tests in folder
# pytest -r prints extra test summary as specified by chars
# pytest -rA prints details of all test cases like 2 passed, 1 failed

def test_case1():
    x = 9
    y = 10
    assert x == y - 1


def test_case2():
    name = "Selenium"
    title1 = "Selenium for web automation"
    assert name in title1


def test_case3():
    name = "jenkins"
    title1 = "Jenkins is CI server"
    assert name in title1 , "Titles doesn't match"  # if fails, prints on screen as AssertionError