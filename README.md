Expression Evaluator:
No extra libraries
Negative number functionality
Pemdas


user input ---> Validate input w/ following requirements:
- No double ++, **
- if --. convert to add
- No text
- Floats
- Valid characters only

Validated input ---> pass through parser
- Parse into: 'value','operator','value' format in list
- Return completed list
- Account for parenthesis. if -(-1-1), I want it returned as: ['-(1'-'1)'] because I want to detect a begin parenthesis 
and strip the number. I want to make sure that if it's a "-(value)", I multiply the result by -1, hence why I want to 
stick the ( with the - sign and value so that I can differentiate from a subtraction operation.

parsed validated input ---> pass through evaluator
