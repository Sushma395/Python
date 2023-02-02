*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Multiple_Test
    open browser     https://www.google.com/     chrome
    maximize browser window
    sleep     2
    open browser     https://www.bing.com/     chrome
    maximize browser window
    sleep     2
    open browser     https://www.yahoo.com/     chrome
    maximize browser window
    #can be done using index(start from 1) or alias
    switch browser      2
    ${title1}=   get title
    log to console    ${title1}

    switch browser    1
    ${title2}=   get title
    log to console    ${title2}

    sleep   2
    close all browsers
