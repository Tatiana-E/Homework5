immutable_var=tuple_=(1, 2, 'sing', True, ['world', 'ocean'])
print(immutable_var)
immutable_var[-1][0]='sky' #можем заменить, т.к. это список внутри картежа
print(immutable_var)
#immutable_var[2]='musik' #не можем заменить, это невозможно
#print(immutable_var)
mutable_list=list_=[1, 2, 'rose', False,]
print(mutable_list)
mutable_list[2]='mirrow'
print(mutable_list)
