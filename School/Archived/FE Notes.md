### Infix to Postfix
- Operands go straight into postfix.
- If placing an item of equal or lower priority to the top of the stack, pop what is in the stack into the postfix BEFORE inserting the current operator.
- Parenthesis are treated as nothing, but once closed, pop all items into the postfix.
- Once the infix string is empty, pop until empty