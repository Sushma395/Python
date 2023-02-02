*** Settings ***
Library     SeleniumLibrary
# keywords placed in resources folder
# resources file will be created where keywords will be placed to attain re-usability
Resource    ../Resources/15_Resources.robot     # implies that reosurces need to be imported from this file


*** Variables ***
${url}      https://demo.guru99.com/selenium/newtours/
${browser}      chrome

*** Test Cases ***
TC1
    LaunchBrowser1
    input text    name:userName     mercury
    input text    name:password     mercury

    LaunchBrowser2      ${url}     ${browser}
    input text    name:userName     mercury2
    input text    name:password     mercury2

    ${title}=    LaunchBrowser3      ${url}     ${browser}
    log to console    ${title}
    log     ${title}    # title wil be logged in report.html file, in test step details
    input text    name:userName     mercury3
    input text    name:password     mercury3
    close all browsers