*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/practice5_resources.robot

*** Variables ***
${url1}      https://demoqa.com/
${browser}      chrome
${url2}     https://www.globalsqa.com/demo-site/

*** Test Cases ***
#to test user defined keywords, browser windows
P5_TC1
    # open browser without arguments
    open browser       ${url1}      ${browser}
    go to    ${url1}/alertsWindows
    Login_P5_1

P5_TC2
    # open browser with arguments
    Login_P5_2      ${url1}     ${browser}
    Log_console

P5_TC3
    # open browser with arguments and return value
    Login_P5_3      ${url2}     ${browser}
    Log_console
    close all browsers

P5_TC4
    #to test browser windows
    open browser    https://www.google.com/     ${browser}
    open browser    https://www.yahoo.com/     ${browser}
    open browser    https://www.bing.com/     ${browser}
    Login_P5_5
    switch browser    2
    Login_P5_5
    switch browser    1
    Login_P5_5
    Login_P5_4
    close all browsers