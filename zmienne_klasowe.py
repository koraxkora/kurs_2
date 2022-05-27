class Test:
    var = 'var_0'
    var_list = []

    @classmethod
    def met_class(cls):
        return 'class method'

    @staticmethod
    def met_static():
        return 'static method'


def r_var(obj, var):
    for i in obj.__dict__.items():
        if i[0] == var:
            return obj, i

print(Test.var, r_var(Test, 'var'))
Test.var = 'var_1'
print("---Test.var = 'var_1'")
print(Test.var, r_var(Test, 'var'))
test_1 = Test()
print("---test_1 = Test()")
print(test_1.var, r_var(test_1, 'var'))
test_1.var = 'var_t0'
print("---test_1.var = 'var_t0")
print(test_1.var, r_var(test_1, 'var'))
print(Test.var, r_var(Test, 'var'))

print('-' * 10)
print(Test.var_list, r_var(Test, 'var_list'))
Test.var_list.append(1)
print("---Test.var_list.append(1)")
print(Test.var_list, r_var(Test, 'var_list'))
test_1.var_list.append(2)
print("---test_1.var_list.append(2)")
print(test_1.var_list, r_var(test_1, 'var_list'))
test_1.var_list = [3]
print("---test_1.var_list = [3]")
test_1.var_list.append(4)
print("---test_1.var_list.append(4)")
print(test_1.var_list, r_var(test_1, 'var_list'))
print(Test.var_list, r_var(Test, 'var_list'))

print(Test.met_class(), r_var(Test, 'met_class'))
print(test_1.met_class(), r_var(test_1, 'met_class'))
print(Test.met_static(), r_var(Test, 'met_static'))
print(test_1.met_static(), r_var(test_1, 'met_static'))
