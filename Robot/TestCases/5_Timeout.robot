*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TimeOut_Test
    open browser    https://demowebshop.tricentis.com/register  chrome
    maximize browser window

    ${time} =   get selenium timeout
    log to console    ${time}

    # Next steps will wait till Register step appears on screen
    wait until page contains    Register    1 seconds
    # Negative test case as registaration is not on page and set timeout
    #timeout only applicable for 'wait until page contains' step
    set selenium timeout    3 seconds

    ${time} =   get selenium timeout
    log to console    ${time}

    wait until page contains    Registration     5 seconds

    select radio button    Gender   F
    input text    id:FirstName      Susheela
    input text    name:LastName     Bandi
    input text    name:Email    asdf@gmail.com
    input text    id:Password   susheeb
    input text    id:ConfirmPassword   susheeb






