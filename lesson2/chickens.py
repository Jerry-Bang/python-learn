
def hundred_chickens():

    for num_cock in range(101):
        for num_hen in range(101):
            num_chicken = 100 - num_cock - num_hen
            #  这个判断是否必须？
            if num_chicken % 3 == 0:
                if 5*num_cock + 3*num_hen + num_chicken/3 == 100:
                    print("cock: " + str(num_cock) + "  hen: " + str(num_hen) + "  chick: "+str(num_chicken))


if __name__ == "__main__":
    hundred_chickens()