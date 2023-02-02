*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Mouse_Operations_Test
    set selenium speed     1 second
    # Right Click Action
    open browser    http://swisnl.github.io/jQuery-contextMenu/demo.html      chrome
    maximize browser window
    open context menu     xpath://span[contains(text(),'right click me')]       # internally performs right click option
    click element    xpath://body/ul[1]/li[7]/span[1]
    handle alert    accept
    # Double Click Action
    go to    https://testautomationpractice.blogspot.com/
    double click element    xpath://button[contains(text(),'Copy Text')]
    # Drag & Drop Action
    go to    http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    maximize browser window
    drag and drop     id:box6      id:box106        # need to locate source & target elements
    drag and drop     id:box3      id:box101
    close browser
