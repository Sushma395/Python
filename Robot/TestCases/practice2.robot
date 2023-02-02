*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC_1
# to practise timeout,wait,speed,alerts,scroll, tabbed windows,
    ${speed} =      get selenium speed
    log to console    before speed = ${speed}
    set selenium speed    1 second
    ${speed} =      get selenium speed
    log to console    after speed = ${speed}

    open browser    https://www.toolsqa.com/     chrome
    click link    xpath://header/nav[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[2]/a[1]
    ${sel_title}=   get title
    log to console   ${sel_title}
    click link    xpath://header/nav[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[3]/a[1]
    switch window     ${sel_title}
    close window

    switch window     main
    maximize browser window
    execute javascript    window.scrollTo(0, document.body.scrollHeight)
    scroll element into view    xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[3]
    click element    xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[3]

    scroll element into view    xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[5]
    ${wait} =      get selenium implicit wait
    log to console    before wait = ${wait}
    set selenium implicit wait    3 seconds
    click element    xpath://body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]
    ${wait} =      get selenium implicit wait
    log to console    after wait = ${wait}
    click button    id:alertButton
    alert should be present    You clicked a button
    handle alert     accept

    ${time_out} =      get selenium timeout
    log to console    default time_out = ${time_out}
    set selenium timeout    2 seconds
    click button    id:timerAlertButton
    ${time_out} =      get selenium timeout
    log to console    after time_out1 = ${time_out}
    # < 5 seconds timout in handle alert, will fail the test case, as alert original time out is 5 seconds
    handle alert     accept     6 second
    ${time_out} =      get selenium timeout
    log to console    after time_out2 = ${time_out}

    execute javascript    window.scrollTo(689,479)
    scroll element into view    id:confirmButton
    set focus to element    id:confirmButton
    element should be focused       id:confirmButton

    click button     id:confirmButton
    handle alert     dismiss
    element should be visible    id:confirmResult
    log to console    You selected cancel is visible

    close browser

