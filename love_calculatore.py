def calculate_love_score(name1,name2):
    true_count=0
    name1=name1.lower()
    for first in name1:
        if first=="t" or first=="r" or first=="u" or first=="e":
            true_count+=1
    for second in name2:
        if second=="t" or second=="r" or second=="u" or second=="e":
            true_count+=1
    
    love_count=0
    for first in name1:
        if first=="l" or first=="o" or first=="v" or first=="e":
            love_count+=1
    for second in name2:
        if second=="l" or second=="o" or second=="v" or second=="e":
            love_count+=1
    true_count=str(true_count)
    love_count=str(love_count)
    combine=true_count+love_count
    print(combine)

calculate_love_score("abhijeet","kimaya")