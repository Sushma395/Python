*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Tabbed_Test
    #open browser     https://demoqa.com/browser-windows    chrome
    open browser     https://demo.automationtesting.in/Windows.html     chrome
    click element    xpath://*[@id="Tabbed"]/a/button
    # switch window can be done using title
    switch window   title=Selenium       #select window deprecated, need to use switch window
    sleep    2
    click element    xpath://span[contains(text(),'Support')]
    sleep    2
    close all browsers


