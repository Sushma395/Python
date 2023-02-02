*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Capture_Screen_Test
    #open browser     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login     chrome
    open browser        https://demoqa.com/     chrome
    maximize browser window
    # Captures a screenshot from the element identified by locator
    capture element screenshot    xpath://header/a[1]/img[1]     C:/Users/suba0816/PycharmProjects/RobotProject/logo.png
    capture page screenshot     C:/Users/suba0816/PycharmProjects/RobotProject/page.png
    # not mentioing path will save screenshot in project itelf, here it's RobotProject
    capture element screenshot    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/a[1]/img[1]     logo2.png
    capture page screenshot     page2.png

