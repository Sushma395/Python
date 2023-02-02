# Settings not needed as it's only for loop explanation
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
@{list}     Sa   Su   Sh    Si

*** Test Cases ***
For_Loop1
    FOR   ${i}    IN RANGE    1   10
    LOG TO CONSOLE   ${i}
    END

For_Loop2
    FOR   ${i}    IN  1 2 3 4 5 6 7 8
    LOG TO CONSOLE    ${i}
    END

For_Loop3
    @{items}    create list    1  2  3  4  5  6
    FOR   ${i}    IN    @{items}
    LOG TO CONSOLE    ${i}
    END

For_Loop4
    FOR    ${i}    IN    john   paul    david   emanuel
    LOG TO CONSOLE    ${i}
    END

For_Loop5
    @{names}   create list    johny   pauly    pavan   emily
    FOR    ${i}    IN    @{names}
    LOG TO CONSOLE    ${i}
    END

For_Loop6
    @{val}      create list      1  2   3   4
    &{dict}     create dictionary    a=@{list}    b=@{val}
    FOR     ${i}    IN    &{dict}
        log to console    ${i}
    END

Exit_Loop
    @{alnum}   create list    a b 1 e 5 7 g
    FOR     ${i}    IN    @{alnum}
        LOG TO CONSOLE    ${i}
        exit for loop if    ${i}==5
    END

