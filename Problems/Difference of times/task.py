hourA = int(input())
minuteA = int(input())
secondA = int(input())
hourB = int(input())
minuteB = int(input())
secondB = int(input())

output = ((hourB - hourA) * 3600) + ((minuteB - minuteA) * 60) + (secondB - secondA)
print(output)
