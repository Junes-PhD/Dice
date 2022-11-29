class user_select:
    def __init__(self) -> None:
        pass
    
    def __str__(self):
        pass

    def dice_num():
        num = input("1-6:")
        try:
            n = int(num)
            if n >= 1 and n <= 6:
                return n
            else:
                user_select.dice_num()
        except:
            user_select.dice_num()

    def mode():
        mode = input("Select Mode:")
        return mode

    def rolls():
        rolls = input("Number of Rolls:")
        return rolls
    
    def agree():
        response = input("Y/N?:")
        if response == "Y" or response == "y" or response == "Yes" or response == "yes":
            return "yes"
        elif response == "N" or response == "n" or response == "No" or response == "no":
            return "no"
        else:
            user_select.agree()
