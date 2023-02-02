*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Practice3_Test
# to practise frames, tabbed windows, browser keywords, screenshot, scroll
    set selenium speed    1 seconds
    open browser    https://demoqa.com/alertsWindows    chrome
    maximize browser window

    execute javascript    window.scrollTo(166, 515)
    #scroll element into view     xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]
    click element    xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]
    select frame      id:frame1
    current frame should contain    This is a sample page

    open browser    https://chercher.tech/practice/frames-example-selenium-webdriver    chrome

    select frame    id:frame1
    current frame should contain    Topic :
    input text    xpath:/html/body/input  This is frame's text box
    execute javascript    window:scrollTo(0,document.body.scrollHeight)
    select frame    id:frame3
    select checkbox    id:a
    unselect frame
    unselect frame

    select frame    id:frame2
    select from list by label    id:animals     Big Baby Cat
    unselect frame

    capture element screenshot    id:frame2
    unselect frame
    capture page screenshot
    close all browsers


