from pwn import remote
from sympy import Eq, solve, sympify

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


# Connect to the remote server
conn = remote('62.173.140.174', 39001)

# Wait until the prompt '>>>' appears
conn.recvuntil(b">>>")

conn.sendline(b"start")

conn.recvuntil(b".\n\n")

for i in range(50):
    try:
        conn.recvuntil(b"/50) ")
        eqn = conn.recvline().decode("utf-8").replace(" ","")
        print(eqn)
        ans = solve_equation(eqn)
        conn.recvuntil(b">>>")
        conn.sendline(ans)
    except:
        print(i,eqn)
        break

conn.interactive()