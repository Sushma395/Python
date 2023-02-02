*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Drop Downs and List Boxes
    open browser    ${url}  ${browser}
    # selecting drop downs by index,value,label
    # label as in visible text
    select from list by label    continents     Australia
    sleep   1
    #index starts from 0
    #North America
    select from list by index    continents     5
    #not possible here as there is no value --> select from list by value
    # selecting from list boxes - multiple values can be selected
    select from list by label    selenium_commands   Browser Commands
    sleep   1
    # WebElement Commands
    select from list by index    selenium_commands  4
    sleep   1
    # unselecting list boxes/drop downs by value index label
    unselect from list by label    selenium_commands   Browser Commands

