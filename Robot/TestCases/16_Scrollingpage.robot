*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Scrolling_Test
    open browser    https://flagpedia.net/index     chrome
    maximize browser window
    set selenium speed     1 second
    # vertical scrolling is applicable for this page
    execute javascript    window.scrollTo(0, 2000)      # (A, B) A, B represents horizontal, vertical scrolling
    # scrolling page till element is found
    scroll element into view    xpath://*[@id="content"]/div/ul[2]/li[104]/a/picture/img
    # scrolling page till bottom of page
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    # to scroll page back to top of page
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)
    close browser


