# ball_colors = ["red" , "blue" , "green" , "blue" , "red" , "yellow"]

# unique_colors = set(ball_colors)

# print(unique_colors)


# union intersection difference 


group_a = {"Alice" , "Bob" , "Charlie"}
group_b = {"Bob" , "Diana" , "Frank"}

# union
all_students = group_a | group_b
print("Students in either group" , all_students)

# intersection

common_students = group_a & group_b
print("Students in both groups" , common_students)

# difference

exclusive_to_a = group_a -  group_b
exclusive_to_b = group_b -  group_a


print("Students only in group a" , exclusive_to_a)
print("Students only in group b" , exclusive_to_b)

