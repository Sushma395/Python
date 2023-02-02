*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Log_console
    ${log_url1}=     get location
    log to console    url=${log_url1}
    close all browsers

Login_P5_1
    maximize browser window
    go back

Login_P5_2
    [Arguments]    ${TC2_url}    ${TC2_browser}
    open browser    ${TC2_url}    ${TC2_browser}
    maximize browser window

Login_P5_3
    [Arguments]    ${TC3_url}    ${TC3_browser}
    open browser    ${TC3_url}    ${TC3_browser}
    maximize browser window
    ${titles}=   get window titles
    [Return]    windowtitles=${titles}

Login_P5_4
    ${titles}=   get window titles
    [Return]    windowtitles=${titles}

Login_P5_5
    ${title}=   get title
    log to console    title=${title}






