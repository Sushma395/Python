*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://demoqa.com/menu
@{lst}  ['Sub Text']

*** Test Cases ***
dropdown_test
    open browser      ${url}    ${browser}
    click element    xpath://a[contains(text(),'Main Item 2')]
    select from list by label     Main Item 2      Sub Item

