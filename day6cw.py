attendance=[18,20,19,15,21]
count_full=0
sum=0
for i in attendance:
    sum += i
    if (i==20):
        print("Full")
        count_full += 1
    elif(i>20):
        print("more students were present")
    else:
        print("Not Full")

print(count_full)
print("total attendance for all five days ", sum)