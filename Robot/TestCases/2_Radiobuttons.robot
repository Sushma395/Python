*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Testing radio Buttons and Check Boxes
    open browser   ${url}    ${browser}
    # wait taime between every command execution
    set selenium speed    2 seconds
    # selecting radio buttons
    select radio button     sex   Female
    select radio button    exp     6
    # selecting check boxes
    select checkbox    id:profession-1
    select checkbox    xpath://input[@id='profession-0']
    unselect checkbox    id:profession-1

