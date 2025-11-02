

marks=[80,72,90,30,10]

total=0 

for mark in marks:

  total += mark
    
average = total/len(marks)
marks.append(60)
marks.remove(min(marks))
marks.remove(max(marks))
print(marks)
print(total)
print(average)
