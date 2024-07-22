# string ar immutable
selfish = "01234567"
selfish = "454545"
selfish += "2323"
print(selfish)  # 100 and mutable or changeable

selfish[0] = '8' # TypeError: 'int' object does not support item assignment
print(selfish)
# can change complexly
# not change any partial
