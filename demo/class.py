def maker(a):
    def action(b):
        return a*b
    return action

f = maker(2)
print(f(3))