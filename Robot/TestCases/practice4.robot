*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Practice4_Test
# to practise mouse operations, drag and drop
    set selenium speed     1 second
    # drag and drop
    open browser    https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager    chrome
    maximize browser window
    select frame     xpath://*[@id="post-2669"]/div[2]/div/div/div[1]/p/iframe
    drag and drop   xpath://*[@id="gallery"]/li[1]    id:trash      #drag and drop to trash
    drag and drop   xpath://*[@id="gallery"]/li[1]    id:trash      #drag and drop to trash
    click element    xpath://*[@id="gallery"]/li[1]/a[2]    #delete to trash
    drag and drop    xpath://*[@id="trash"]/ul/li[1]     id:gallery
    click element      xpath://*[@id="trash"]/ul/li[1]/a[1]    #zoomin
    element should contain     xpath://*[@id="ui-id-2"]     The peaks of High Tatras
    capture element screenshot      xpath://*[@id="ui-id-1"]
    click button     xpath:/html/body/div[3]/div[1]/button     #close zoomin
    click element     xpath://*[@id="trash"]/ul/li[2]/a[2]    #recycle

    # right click
    go to    http://swisnl.github.io/jQuery-contextMenu/demo.html
    open context menu    xpath:/html/body/div/section/div/div/div/p/span
    click element      xpath:/html/body/ul/li[1]
    alert should be present     clicked: edit    #accepts alert by default

    open context menu    xpath:/html/body/div/section/div/div/div/p/span
    element should be visible     xpath:/html/body/ul/li[7]
    click element     xpath:/html/body/ul/li[7]
    handle alert    accept

    # double click
    go to       https://testautomationpractice.blogspot.com/
    double click element     xpath://*[@id="HTML10"]/div[1]/button

    close all browsers

