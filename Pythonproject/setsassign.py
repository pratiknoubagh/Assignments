#ans1:
language={"C","C++","JAVA",".NET","Python","R"}
language.add("KOTLIN")
print(language)

#ans2:
language.remove("R")
print(language)
print("Is Python present in the set","Python" in language)

#ans3:
language1={"C","Python","JAVA","R","C#","PHP","Ruby"}
intersection=language.intersection(language1)
print(intersection)
