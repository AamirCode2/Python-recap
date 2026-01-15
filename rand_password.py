import random
import string

def create_random_password(length):
    x = list()
    num_played = 0

    for i in range( length):
        num = str(random.randint(0, 9))
        x.append(num)

        num_played+=1
        if num_played == length:
            break

        lower_str = (random.choice(string.ascii_lowercase))
        x.append(lower_str)
        num_played+=1

        if num_played == length:
            break

        upper_str = (random.choice(string.ascii_uppercase))
        x.append(upper_str)
        num_played+=1

    random.shuffle(x)
    return "".join(x)

intro = input("Do you want a random password with lowercase and uppercase characters and digits? (Y/N) ")
if intro == "Yes" or intro == "Y" or intro == "y" or intro == "yes":
    length = int(input("What length do you want your password to be? "))
    random_password = create_random_password(length)
    print(f"\nHere is your random password: {random_password}")