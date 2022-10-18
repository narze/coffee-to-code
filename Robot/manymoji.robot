*** Settings ***
Library     String

*** Variables ***
${intial_text}  coffee

*** Keywords ***
Convert coffee to code
    Log to console   Show the first label: ${intial_text} 
    ${str} =	Replace String Using Regexp	   ${intial_text}  (ffe)  d
    Log to console   Print final result: ${str}
    
*** Test Cases ***
Indicate coffee to code by robot framework
    [Tags]  coffee_to_code
    Convert coffee to code