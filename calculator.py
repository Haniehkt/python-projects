
def format_name(fname,lnam):
   
    # print(f"the firstname is:{fname} and the lastname is {lnam}")
    fotmatted_fname=fname.title()
    formatted_lname=lnam.title()
    return fname,lnam
print(format_name(input("fname")),input("lname"))
