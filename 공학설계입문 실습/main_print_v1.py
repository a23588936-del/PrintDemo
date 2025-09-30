name = "Alice"
age = 25
score = 95.5

print("Hello, Python!")

print("Name:",name,"Age:", age, "Score:",score)

print("My name is {name}, i am {age} years old, score: {score}")

print("My name is {}, i am {} years old, score: {}". format(name, age, score))
print("My name is {0}, i am {1} years old, score: {2}". format(name, age, score))
print("score with 2 decimals: {:.2f}".format(score))

print("Name: %s, Age: %d, Score: %.1f" %(name, age, score))

print("This is line 1&nThis is line 2")

print("Hello", end=" ")
print("World!")

print("2025","09","23",sep="-")

data = {"name" : name, "age" : age, "score": score}
print("Date:" , data)

print(f"Next year age: {age + 1}")
print(f"score (rounded): {round(score)}")

print(f"""
Student Info:
 - Name :{name}
 - Age : {age}
 - Score: {score: .2f}
 """)
