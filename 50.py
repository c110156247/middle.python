students=set(['john','mary','tina','fiona','claire','eva','ben','bill','bert'])
english=set(['john','mary','fiona','claire','ben','bill'])
math=set(['mary','fiona','claire','ben','eva'])
print('英文數學都及格'+str(students&english))
x=students-math
print('數學不及格'+str(x))
print('英文及格且數學不及格'+str(english&x))