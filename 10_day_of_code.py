# def format_name(f_name,l_name):
#     return f_name.title()+" "+l_name.title()
# formated_string=format_name("saurabh","kamane")
# print(formated_string)
# print(len("saurabh"))
# def function_2(text):
#     return text.title()
# output=function_2("saurabh")
# print(output)
#multiple return values in the functions
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "you did not provide valid input"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("enter first name"),input("enter last name")))