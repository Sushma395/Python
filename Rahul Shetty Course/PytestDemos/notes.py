# --demo1--
# Any pytest file should start with test_or end with _test
# pytest method names should start with  test
# any code should be wrapped in method only
# py.test or pytest on command line to run all tests in folder
# pytest -v provides more info on logs
# pytest -s to get logging on screen

# --demo2--
# py.test -k add --> to run all test cases having add in name
# -k defines regular expression
# pytest <file_name> to run specific file
# py.test <file_name>
# method name should make sense
# @pytest.mark.smoke --> mark test case
# -m to run tests with mentioned mark (here pytest -m smoke)
# @pytest.mark.skip to skip test case
# @pytest.mark.xfail to xpass a test case

# --demo3--
# fixtures for setup & teardown
# @pytest.fixture()
# pass fixture method name as argument to call fixture
# yield to separate setup & teardown defined in same method

# to avoid duplicating fixtures, for all test files, conftest.py can be used
# move fixtures to conftest.py if fixture is shared by multiple files

# @pytest.mark.usefixtures("fixture_name") --> here fixture_name = setup
# if we warp all test cases under class, can use above command instead of calling fixture again and again
# @pytest.fixture(scope="class") --> mention this in conftest.py when fixture is called in a class
# when we define fixture scope to class only, it will run once before the class is initiated and at the end

# --demo4--
# since dataLoad needs to be returned, it should be passed in method argument
# ex: @pytest.mark.usefixtures("dataLoad")

# parametrization in fixtures
# params is used as argument for fixture parametrization
# @pytest.fixture(params=[.....])
# request is an instance that belongs to fixture
# ex: --demo5--
# parameterization and datadriven can be done with return in tuple format

# html report generation
# https://pypi.org/project/pytest-html/
# pip install pytest-html
# pytest --html=report.html --> syntax to create report

# --demo6--
# logging
# if level is set to warning, logger will print from warning till last level(critical) only
# refer demo for hierarchy
# log printed in mentioned file

# Base Class
# Base Class created and used as parent class in demo 4 for test case 2
# whatever passed into log.info here, is returned on report when pytest --html=report.html  is used while executing script
# print statement output will not be returned on report.html

# Logger object can be created by inheriting parent class (here BaseClass) and using the method

