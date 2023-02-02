*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
AlertsHandling_Test
    #open browser    https://demoqa.com/alerts   chrome
    open browser    https://chercher.tech/practice/practice-pop-ups-selenium-webdriver      chrome
    set selenium speed    1 second
    click element    name:alert     #opens alert
    # 3 types of alerts handling available - accept dismiss leave
    handle alert    accept      #clicks on ok button on alert
    click element    name:confirmation
    handle alert    dismiss     #clicks on cancel button on alert
    #click element    name:prompt
    #handle alert    leave       #leaves the alert open
    click element    name:alert     #opens alert
    #verifying message on alert
    alert should be present     I am alert
    #alert should not be present     I am alert

