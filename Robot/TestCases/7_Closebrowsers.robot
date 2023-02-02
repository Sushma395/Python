*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Close_All_Browsers_Test
    open browser    https://demowebshop.tricentis.com/register  chrome
    maximize browser window

    open browser    https://www.techlistic.com/p/selenium-practice-form.html    chrome
    maximize browser window

    #latest browser opened will be closed
    close browser

    open browser    https://automationexercise.com/     chrome
    maximize browser window

    #all browsers opened will be closed
    close all browsers