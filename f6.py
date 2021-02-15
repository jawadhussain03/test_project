import f3

x = f3.Cutils('uname -a')
print(x.output())
y = f3.Cutils('uname -r')
print(y.output())
