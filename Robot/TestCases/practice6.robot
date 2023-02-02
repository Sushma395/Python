*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${count}     0
@{list}     Sa   Su   Sh    Si


*** Test Cases ***
#to practise for loop
TC1
    FOR     ${a}    IN RANGE    10  13
    log to console     ${a}
    END

TC2
    FOR    ${b}     IN   Suhas   Sushi   Shie    Susheel
    log to console    ${b}
    END

TC3
    FOR    ${b}     IN      @{list}
    log to console    ${b}
    END

TC4
    @{val}      create list      1  2   3   4
    &{dict}     create dictionary    a=@{list}    b=@{val}
    FOR     ${i}    IN    &{dict}
        log to console    ${i}
    END

TC5
    FOR    ${c}     IN       S   O   A    P
    log to console     ${c}
    ${count}=    evaluate    ${count}+1
    log to console     count=${count}
    exit for loop if    ${c}== S
    log to console    S Found
    END
