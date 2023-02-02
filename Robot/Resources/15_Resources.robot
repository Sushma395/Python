*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
# make the arguments of certain test functions easier to invoke
# reduce the amount of coding required for new test cases
# resources file will be created where keywords will be placed to attain re-usability

# simple user-defined keyword with no arguments
LaunchBrowser1
    open browser     ${url}     ${browser}
    maximize browser window
# simple user-defined keyword with arguments
# values of launchbrowser2 - test case argumets will be stored into LaunchBrowser2 arguments
LaunchBrowser2
    [Arguments]    ${app_url}   ${app_browser}
    open browser    ${app_url}   ${app_browser}
    maximize browser window
# simple user-defined keyword with arguments and returns value
LaunchBrowser3
    [Arguments]    ${app_url2}   ${app_browser2}
    open browser    ${app_url2}   ${app_browser2}
    maximize browser window
    ${app_title}=   get title
    [Return]    ${app_title}
