# Great Mathematician
## Category : Misc
## Points : 200

A tcp socket was given(62.173.140.174:39001).Connected to the tcp socket and started the game.

The game asked the answer to 50 linear equations of one variable.However each question must be solved in 5 seconds. Else __TIMED OUT !!!__

So,I used python's `sympy` module and solved the equations using `Eq, solve, sympify`.

```py
def solve_equation(equation_str):
    # Parse the equation and extract variables and constants
    x, equals, result = equation_str.partition('=')

    # Parse the equation into a sympy equation
    equation_sympy = Eq(sympify(x), sympify(result))

    # Solve the equation
    solution = solve(equation_sympy)

    # Assuming the equation is linear, there should be only one solution
    if len(solution) == 1:
        return str(solution[0])
    else:
        return None  # Unable to solve
```

And wrote the rest of the script to connect handle input and send strings accordingly.

Flag:
```
CODEBY{m4th_t34ch3r_pr0ud_0f_y0u_m4n}
```
