import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()
len_a=len(a)
len_b=len(b)

answer=[0]*len_a
for i in range(len_b):
    cnt=0
    for j in range(len_a):
        if cnt<answer[j]:
            cnt=answer[j]
        elif b[i]==a[j]:
            answer[j]=cnt+1
        
print(max(answer))