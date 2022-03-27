family={"Parents":{"Father":"Aamir Anwer","Mother":"Rubina Aamir"},
        "Siblings":{"Sisters":["Ramsha","Narmeen","Uzma","Aatra"],"Brother":"Sadiq"}}

for i in family.items():
    print(i)

extended= {"Paternal":{"Grandparents":{"Grandfather":"Anwer Shafi","Grandmother":"Safia Anwer"},
                      "Relatives":{"Uncle":"Arif","Aunties":["Saiqa","Shazia","Asiya","Shaista"]}},
           "Maternal":{"Grandparents":{"Grandfather":"Siddique","Grandmother":"Mukhtari"},
                      "Relatives":{"Uncle":["Fayaz","Shafiq","Atiq"],"Aunties":["Samina","Hina"]}}}


print("\n","UPDATED:","\n")

family.update(extended)

for i in family.items():
    for k in i:
        print(k)
