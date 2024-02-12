def hello(): 
    print("hello user!")
    
def pack(fname, mname, lname):
    return [fname, mname, lname]


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        for index in range(len(lunch_list)):
            if index == 0:
                print(f"first i eat {lunch_list[0]}")
            else:
                print(f"next i eat {lunch_list[index]}")
                

hello()

print(pack("David", "Charles", "Thomas"))
eat_lunch([])
eat_lunch(["Ham Sub"])
eat_lunch(["granola", "yogurt", "Ham Sub", "Ice Cream"])