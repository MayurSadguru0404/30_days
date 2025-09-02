def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = int(operand1 / operand2)
          
            stack.append(result)
    
    return stack.pop()

input_expression = "2 1 + 3 *"
output_result = evaluate_postfix(input_expression)
print(f"Input: \"{input_expression}\"")
print(f"Output: {output_result}")
