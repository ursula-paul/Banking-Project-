fruits = ['apple', 'mango', 'cherry', 'banana']

for fruit in fruits:
    print (fruit)
    
for i in range (1,11):
    print (i)
    
word = 'hello'

for letter in word:
    print(letter)
    
    
count = 1
while count <=5 :
    print(count)
    count +=1


response = ""
while response != "yes" and response != "no":  # Continue asking until we get 'yes' or 'no'
    response = input("Do you want to continue? (yes/no): ")
    if response != "yes" and response != "no":
        print("Invalid input. Please type 'yes' or 'no'.")
print("You chose:", response)
