name = "Mohammad Shahriar Hosen"
print(name[0], end='\n')
print(name[0:8], end='\n') # start at 0 and stop at 8-1
print(name[0:8:1], end='\n') # start at 0 and stop at 8-1
# [start:stop:stepover]
for i in name:
    print(i, end=" ")

# slicing
selfish = "0123456789"  # step over is skip
print(selfish[0:9:2])  # 0 2 4 6 8
print(selfish[1:])  # start from 1 and to end
print(selfish[:5])  # start from 5 and to end at 0

print(selfish[::1])  # full with step 1
print(selfish[::2])  # full with step 2
print(selfish[-1])  # last
print(selfish[::-1])  # reverse
