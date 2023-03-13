import random 

paper ='''
  Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)

'''

rock = '''

 Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)

'''

scissors ='''
  Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''




 

#My choice 
my_choice = input('Type "0" for rock , type "1" for scissors ,type "2" for paper ')
print(my_choice)
if my_choice == "0":
 print(rock)
elif my_choice == "1":
 print(scissors)
else:
 print(paper)

 #Computer choice 

choices = [rock , paper, scissors]
choices_length = len(choices)
choices_random_index = random.randint(0, choices_length-1)
random_choice = choices[choices_random_index]
print(random_choice)


# if  my_choice == "0" and random_choice[2] or my_choice == "1" and random_choice[1] or my_choice == "2" and random_choice[0]:
#  print('You win')
# elif random_choice[0] and my_choice=="1" or random_choice[1]and my_choice =="0" or random_choice[2] and my_choice=="2":
#  print('Computer wins')
# elif random_choice[0] and my_choice == "0" or random_choice[1] and my_choice == "2" or random_choice[2] and my_choice == "1":
#  print('Equal')


