
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

#count occurance of 't', 'r', 'u', 'e' in name1
count_t_name1 = name1_lower_case.count("t")
count_r_name1 = name1_lower_case.count("r")
count_u_name1 = name1_lower_case.count("u")
count_e_name1 = name1_lower_case.count("e")


#count occurance of 't', 'r', 'u', 'e' in name2
count_t_name2 = name2_lower_case.count("t")
count_r_name2 = name2_lower_case.count("r")
count_u_name2 = name2_lower_case.count("u")
count_e_name2 = name2_lower_case.count("e")


#"e" is common in both words 'true' and 'love'. So it is counted once and used to find the value of occurance in both words
#count occurance of 'l', 'o', 'v' in name1
count_l_name1 = name1_lower_case.count("l")
count_o_name1 = name1_lower_case.count("o")
count_v_name1 = name1_lower_case.count("v")

#count occurance of 'l', 'o', 'v' in name2
count_l_name2 = name2_lower_case.count("l")
count_o_name2 = name2_lower_case.count("o")
count_v_name2 = name2_lower_case.count("v")


# add occurance of 't', 'r', 'u', 'e' in name1 and name2
true_count = count_t_name1 + count_r_name1 + count_u_name1 + count_e_name1 + count_t_name2 + count_r_name2 + count_u_name2 + count_e_name2
# add occurance of 'l', 'o', 'v', 'e' in name1 and name2
love_count = count_l_name1 + count_o_name1 + count_v_name1 + count_e_name1 + count_l_name2 + count_o_name2 + count_v_name2 + count_e_name2
love_calculator = int(str(true_count) + str(love_count))
# print(love_calculator)


if love_calculator < 10 or love_calculator >90:
    print(f"Your score is {love_calculator}, you go together like coke and mentos.")
elif love_calculator >= 40 and love_calculator <= 50:
    print(f"Your score is {love_calculator}, you are alright together.")
else:
    print(f"Your score is {love_calculator}.")

