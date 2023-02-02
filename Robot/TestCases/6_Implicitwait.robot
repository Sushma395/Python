*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Implicit_Wait_Test
    open browser    https://demowebshop.tricentis.com/register  chrome
    maximize browser window

    ${wait} =   get selenium implicit wait
    log to console    ${wait}

    #applicable for all steps once set
    set selenium implicit wait    5 seconds

    ${wait} =   get selenium implicit wait
    log to console    ${wait}

    select radio button    Gender   F
    # incorrect id provided so that step will fail
    input text    id:FirstName1      Susheela
    input text    name:LastName     Bandi
    input text    name:Email    asdf@gmail.com
    input text    id:Password   susheeb
    input text    id:ConfirmPassword   susheeb






