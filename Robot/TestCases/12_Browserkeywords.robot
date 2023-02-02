*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Browser_Navigation_Test
    set selenium speed     1 second
    open browser        https://www.google.com/     chrome
    ${loc}=     get location        #gets current url
    log to console    ${loc}
    # navigates current browser to new url
    go to    https://www.bing.com/
    ${loc}=     get location        #gets current url
    log to console    ${loc}
    # navigates current browser back to old url
    go back
    ${loc}=     get location        #gets current url
    log to console    ${loc}


