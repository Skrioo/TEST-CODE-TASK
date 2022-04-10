
def get_commission(date_str):
    '''
    Function for checking what commision will be depending on if it's high season or not.
    
    :date_str format: "YYYY-MM-DD" 
    '''
    #Spliting input string into 3 variables
    try:
        [year, month, day] = date_str.split("-")
    except:
        print("Wrong date string format")
        return

    # Checking format and converting month variable to integer so it can be worked with
    if len(year) != 4:
        print("Wrong year input")    
        return
    if len(month) != 2 or int(month) not in range(1,13):
        print("Wrong month input")
        return
    month = int(month)
    if len(day) != 2 or int(day) not in range(1,32):
        print("Wrong day input")
        return
    # Getting the commission value depending on the month
    if (9 >= month >= 6):
        return 0.15
    
    return 0.1

    
