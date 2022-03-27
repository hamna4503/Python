week_dish = {"Monday":"Biryani","Tuesday":"Daal","Wednesday":"noodles",
             "Thursday":["qeema","fruits"],"Friday":"shawarma","Saturday":"qourma",
             "Sunday":"steak"}
choice_dish = {"fastfood":["pizza","burger","shawarma"],
               "desi":["Biryani","qourma","nehari","handi"],
               "other":["steak","sizzling","fruits","pie"],}
dishes_next_week =0
for i in week_dish.values():
    if type(i)!= list:
         for k in choice_dish.values():
            if i == k:
                print(i, "\n")
                dishes_next_week +=1
            else:
                for j in k:
                    if j==i:
                        print(i,"\n")
                        dishes_next_week += 1
    else:
        for h  in i:
            for k in choice_dish.values():
                if h == k:
                    print(h, "\n")
                    dishes_next_week += 1
                else:
                    for j in k:
                        if j == h:
                            print(h, "\n")
                            dishes_next_week += 1
print("The number of dishes next week of "
      "your choice are",dishes_next_week)