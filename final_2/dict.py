def addLine(d,line):
    d = {}
    line = line.lower()
    print(line)
    d.setdefault(0,line)
    
print(addLine(d, "Four for you, Glenn Coco! You go, Glenn Coco!"))
print(addLine(d,"I will travel across the land, searching far and wide. Each Pokemon to understand the power that's inside!"))