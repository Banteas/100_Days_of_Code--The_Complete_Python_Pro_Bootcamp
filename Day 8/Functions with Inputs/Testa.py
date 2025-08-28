def calculate_love_score(name1,name2):
    whole_name = (name1 + name2).lower()
    true_sum = 0
    love_sum = 0
    for char in whole_name:
       if char in "true":
           true_sum += 1
    for char in whole_name:
        if char in "love":
            love_sum += 1
    print(f"{true_sum}{love_sum}")

calculate_love_score("Amalia Konstantinidou","Konstantinos Bantakis")

my_string = "Hello, world! I love the world."
count_l = my_string.count("l")
print(type(count_l))