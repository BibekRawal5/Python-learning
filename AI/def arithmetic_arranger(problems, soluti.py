def arithmetic_arranger(problems, solution = False):
  #error checking
  if len(problems) > 5:
    return "Error: Too many problems."

  first_operands = []
  second_operands = []
  operators = []
  
  for problem in problems:
    f,o,s = problem.split()
    first_operands.append(f.strip())
    second_operands.append(s.strip())
    operators.append(o.strip())
    
  if "*" in operators or "/" in operators:
    return "Error: Operator must be '+' or '-'."
  
  if any([len(i) > 4 for i in first_operands]) or any([len(i) > 4 for i in second_operands]):
    return "Error: Numbers cannot be more than four digits."
  
  if any([not i.isnumeric() for i in first_operands]) or any([not i.isnumeric() for i in second_operands]):
    return "Error: Numbers must only contain digits."

  line1 = ""
  line2 = ""
  line3 = ""
  answers = ""
  
  for i in range(len(problems)):
    max_len = max([first_operands[i], second_operands[i]], key = len)
    max_len = len(max_len)
    line1 += " " * (max_len + 2 - len(first_operands[i])) + first_operands[i]
    line2 += operators[i] + " " * (max_len + 1 - len(second_operands[i])) + second_operands[i]  
    line3 += "-" * (max_len + 2)
    
    if (i + 1) != len(problems):
      line1 += 4 * " "
      line2 += 4 * " " 
      line3 += 4 * " "   
    

    if solution:
      f,s = int(first_operands[i]), int(second_operands[i])
      if operators[i] == "+":
        answer = f + s
      else:
        answer = f - s

      answers += " " * (max_len + 2 - len(str(answer))) + str(answer)
      if (i + 1) != len(problems):
        answers += 4 * " "

  line1 += "\n"
  line2 += "\n"
  

  if solution:
    line3 += "\n"
    return (line1 + line2 + line3 + answers)
  else:
    return (line1 + line2 + line3)
    

    

  

  
  
  
  