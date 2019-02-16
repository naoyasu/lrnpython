answer = input("What is your favorite color?")
with open("color.txt", "w") as f:
    f.write(answer)
