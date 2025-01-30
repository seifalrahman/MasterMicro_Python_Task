from sympy import Symbol,Eq,solveset,solve,nsolve,lambdify,sympify, symbols, simplify, diff, integrate ,S, ConditionSet,Reals,zoo
import matplotlib.pyplot as plt
import numpy as np
import re


def replace_log(expression):
    """
    Replaces all occurrences of 'logN(x)' in the input string with 'log(x, N)' where N is any base.

    Parameters:
        expression (str): The input string containing the mathematical expression.

    Returns:
        str: The modified string with 'logN(x)' replaced by 'log(x, N)'.
    """
    # Use a regular expression to find all occurrences of 'logN'
    modified_expression = re.sub(r'log(\d+)\((.*?)\)', r'log(\2, \1)', expression)
    return modified_expression

def insert_multiplication_operator(equation):
    """
    Replaces instances like '2x' with '2*x' in the equation.
    Replaces instances like '2(x)' with '2*(x)' in the equation.
    """

    equation = re.sub(r"(\d+)([a-zA-Z])", r"\1*\2", equation)
    equation = re.sub(r"(\d+)([(])", r"\1*\2", equation)
    return equation

initial_guesses=[]

for i in range(1 , 1000,1) :
    initial_guesses.append(i)

def drawInfoFunctions (exp,Resolution):
    x = Symbol('x')
    expression=replace_log(exp)
    expression=insert_multiplication_operator(expression)
    expression= sympify(expression)
    diffExp= diff(expression,x)
    diffExp = lambdify(x, diffExp)
    integratedExp = integrate(expression, x)
    integratedExp = lambdify(x, integratedExp)
    x_vals = list(np.linspace(-100, 100, Resolution))
    y1=[]
    y2=[]
    for value in x_vals :
        y1.append(diffExp(float(value)))
        y2.append(integratedExp(float(value)))
    return [x_vals,y1,y2]










def drawUserFunctions (exp1, exp2,Resolution):
    x = Symbol('x')
    expression1=replace_log(exp1)
    expression1 = insert_multiplication_operator(expression1)
    expression1= sympify(expression1)
    expression2=replace_log(exp2)
    expression2 = insert_multiplication_operator(expression2)
    expression2 = sympify(expression2)
    intersection_eq = Eq(expression1, expression2)
    intersection_roots = solveset(intersection_eq,x,domain=S.Reals)# :  solve(intersection_eq, x)
    flag=0

    if  intersection_roots == Reals :
        flag = 1
        intersection_roots = []
    elif not isinstance(intersection_roots, ConditionSet) :
        intersection_roots=[]
        tmp = solveset(intersection_eq, x, domain=S.Reals)  # :  solve(intersection_eq, x)
        for r in tmp :
            if r.is_real :
                intersection_roots.append(r)

    else:
        intersection_roots = []
        for i in range(0,len(initial_guesses)):
            guess= nsolve(intersection_eq, x, initial_guesses[i])
            if guess.is_real :
                intersection_roots.append(guess)

        #intersection_roots.append(nsolve(intersection_eq, x, 0.01))
        flag=1
        # for root in intersection_roots:
        #     if not root.is_real :
        #         intersection_roots=[]

    if expression1 ==zoo or expression2 ==zoo :
        raise ValueError
    expression1= lambdify(x, expression1)
    expression2=lambdify(x, expression2)

    x_vals=[]
    if flag==1 :
        x_vals=list (np.linspace(-100,100,Resolution))

    elif len(intersection_roots)>1  :
        extension =intersection_roots[len(intersection_roots)-1]-intersection_roots[0]
        x_vals=list(np.linspace(int(intersection_roots[0]-extension),int(intersection_roots[0]),Resolution))
        #you don't have to append in numpy array because it creates new array each time because Numpy array has a fixed size
        for i in range(0,len(intersection_roots)-1):
            x_vals+=list(np.linspace(int(intersection_roots[i]),int(intersection_roots[i + 1]),Resolution))

        x_vals+=list(np.linspace(int(intersection_roots[len(intersection_roots)-1]),int(intersection_roots[len(intersection_roots)-1]+extension),Resolution))
    elif len(intersection_roots)==1 :
        x_vals= list(np.linspace(int(intersection_roots[0]-20),int(intersection_roots[0]+20),Resolution))
    else:
        x_vals = list(np.linspace(-100, 100, Resolution))



    y1=[]
    y2=[]
    for value in x_vals :
        y1.append(expression1(float(value)))
        y2.append(expression2(float(value)))
    points_to_annotate=[]
    if  not isinstance(intersection_roots, ConditionSet) :
        for root in intersection_roots :
            points_to_annotate.append((float(root) , expression1(float(root))))

    return  [x_vals,y1,y2 , points_to_annotate]




    # numerical_function = lambdify(x, expression)
    # To specify Where to draw I have to get the solution first
