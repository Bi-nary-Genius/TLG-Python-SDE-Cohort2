#Part 1

vampycount = 0

with open("dracula.txt","r") as fileobj:

#Part 2
for line in foo:
    print(line)

#Part 3
for line in foo:
    if "vampire" in line:
        print(each_line.strip)

#Part 4
for line in foo:
    if "vampire" in line.lower():
        print(line)

#Part 5
count = 0
for line in foo:
    if "vampire" in line.lower():
        count +=1
        print(count)

#Part 6
counter= 0

with open("dracula.txt","r") as foo:
    with open("vampytimex.txt","w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                counter += 1
                fang.write(line)

print(counter)

