def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    var18 = var9(arg1, arg2)
    var26 = func9(arg1, var18)
    var31 = func10(var6, var26)
    if var31 < arg2:
        var32 = arg1 & var26 & arg1
    else:
        var32 = 4 ^ arg2
    result = arg1 - 1507546464
    return result
def func10(arg27, arg28):
    var29 = 0
    for var30 in xrange(8):
        var29 += arg28 - (arg28 + -1)
    return var29
def func9(arg19, arg20):
    var21 = arg19 ^ arg20
    var22 = -710700585 + ((var21 ^ arg19 | -2134364992) & (-856726454 | (((-872 + arg19) & 337872567 - (var21 & arg20)) - arg19)) & arg19)
    var23 = ((var21 & 973 - (arg19 - arg19) & var22) ^ 165139962) | arg20
    var24 = var23 + (arg20 - (var23 - var22) & ((var23 & var23 | var23 & 646) + arg20))
    var25 = arg20 ^ -11 ^ 293
    result = -566 | arg19
    return result
def func6(arg10, arg11):
    var14 = class7()
    for var15 in range(8):
        var14.func8(arg10, arg10)
    var16 = (-217 ^ arg10) & 472 + arg10 & ((99 + 858 | arg11) ^ 794)
    var17 = var16 + arg11 | -1341685251
    result = var16 ^ var16 | (-1441387951 | var17 ^ -2138343118 ^ (var17 ^ var16) & (arg11 + arg10) + var16) + var16 | arg10
    return result
class class7(object):
    def func8(self, arg12, arg13):
        return 0
def func5():
    closure = [-1]
    def func4(arg7, arg8):
        closure[0] += func6(arg7, arg8)
        return closure[0]
    func = func4
    return func
var9 = func5()
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = 4 + rest
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 33'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
