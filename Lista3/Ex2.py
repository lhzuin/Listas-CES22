def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "********************************************\n{0}********************************************".format(func(*args, **kwargs))
    return func_wrapper

@p_decorate
def get_names(*args, **kwargs):
    txt = ""
    for i in args:
        txt += i+"\n"
    return txt

@p_decorate
def list_info(*args,**kwargs):
    txt = ""
    for i in kwargs.keys():
        txt += f'{i}:\t{kwargs.get(i)}\n'
    return txt

print (get_names("John", "Paul", "Mary"))
print("\n\n")
print(list_info(name1 = "John", grade1 = 7, name2 = "Peter", grade2 = 9))