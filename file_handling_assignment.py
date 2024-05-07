with open("my_file.txt", "w") as file:
    file.write("I am a Royal Priesthold\n")
    file.write("A perculiar person\n")
    file.write("500, 200, 500")
with open("my_file.txt", "r") as fa:
    print(fa.read())
try:
    print("I am not perfect yet, but i will soon become the best")
except:
    print("I am the best")
finally:
    print("Glory be to God the King")