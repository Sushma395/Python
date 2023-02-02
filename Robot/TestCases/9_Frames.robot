*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Frames_Test
    #open browser    https://chercher.tech/practice/frames-example-selenium-webdriver    chrome
    open browser     https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html   chrome
    sleep    2
    # many frames can be present in one web page
    # need to 'select frame' --> action followed by-->  unselect frame before moving to next frame in page
    select frame    name:packageListFrame
    click link    org.openqa.selenium
    unselect frame
    sleep    2
    select frame    packageFrame
    click link      WebDriver
    unselect frame
    sleep    2
    select frame    classFrame
    click link     Help
    sleep    2
    click link     Index
    unselect frame