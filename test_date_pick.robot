*** Settings ***
Library    SeleniumLibrary
Library    date_picker.DatePicker


*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Set Window Position   ${2000}    ${0} 
    Maximize Browser Window
    
*** Variables ***
${url}    https://demoqa.com/date-picker
${browser}    chrome
&{date_dict}    Month=May    Year=${1997}    Day=${30}
&{date_time_dict}    Month=May    Year=${1997}    Day=${30}    Hour=${10}    Minute=${40}

*** Test Cases ***
TestSelectDate
    Open Browser Page
    Select Date    ${date_dict}
    Sleep    3
    Close Browser
   
TestInsertDateAsString
    Open Browser Page
    Input Date    ${date_dict}
    Sleep    3
    Close Browser

TestInsertDateAndTimeAsString
    Open Browser Page
    Input Date Time   ${date_time_dict}
    Sleep    5
    Close Browser
    
