*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${browser}     chrome
${url}      https://demowebshop.tricentis.com/register

*** Test Cases ***
Speed_Test
    #to get default selenium speed
    ${speed} =   get selenium speed
    log to console    ${speed}
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed    1second    #-->to make this sleep time applicable for all steps

    select radio button    Gender   F
    # to pause execution on below step for mentioned duration
    sleep     3    #-->applibale only for this step

    input text    id:FirstName      Susheela
    input text    name:LastName     Bandi
    input text    name:Email    asdf@gmail.com
    input text    id:Password   susheeb
    input text    id:ConfirmPassword   susheeb
    #to find final selenium speed
    ${speed} =   get selenium speed
    log to console    ${speed}




