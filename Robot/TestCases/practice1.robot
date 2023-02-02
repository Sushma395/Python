*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Practise1
# input text, click button, open browser, radio button, set variable, select from list by *, select select checkbox
# unselect, choose file, close browser, sleep, set selenium speed,  element should be visible
    open browser    ${url}  ${browser}
    set selenium speed    1second
    input text    name:firstname    sush
    input text    name:lastname     b
    select radio button    sex    Female
    select radio button    exp     6
    ${d_p}    set variable    id:datepicker
    element should be visible   ${d_p}
    input text    ${d_p}     17/9/2022
    select checkbox    id:profession-1
    select checkbox    id:tool-2
    select checkbox    id:tool-0
    unselect checkbox    id:tool-0
    select from list by label    continents     Europe
    select from list by index    selenium_commands      3
    unselect from list by index    selenium_commands      3
    sleep   1
    select from list by label    selenium_commands      Browser Commands
    choose file   class:input-file  C:/Users/suba0816/PycharmProjects/pythonProject/Programs/test.docx
    #click link    xpath://a[contains(text(),'Click here to Download File')]
    click button    xpath://button[@id='submit']
    close browser


