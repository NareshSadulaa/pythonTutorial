def person():
    print("A person is walking....")
    for i in range(5):
        if i == 3:
            user = input("Are you tired?  ")
            if user == "y" or user == "yes" or user == "YES" or user == "Y" or user == "Yes":
                print("Take Rest..")
                break
            else:
                print("Okiee, then continue Walking")
        else:
            continue
person()
