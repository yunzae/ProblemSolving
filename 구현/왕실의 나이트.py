myinput=input()
row_list=['a','b','c','d','e','f','g','h']
row=myinput[0]
column=int(myinput[1])
row1=0
row2=0
col1=0
col2=0

for i in range(len(row_list)):
    if row_list[i]==row:
        row_num=i+1


row_check2=[row_num+2, row_num-2]   # 좌우 두칸check
row_check1=[row_num+1, row_num-1]   # 좌우 한칸
column_check2=[column+2,column-2]   # 위아래 두칸
column_check1=[column+1,column-1]   # 위아래 한칸


# 위아래 좌우 가능한지 check
for i in row_check1:
    if 0<i<9:
        row1+=1

for i in row_check2:
    if 0<i<9:
        row2+=1

for i in column_check1:
    if 0<i<9:
        col1+=1

for i in column_check2:
    if 0<i<9:
        col2+=1


#2칸,1칸 이동이니 가능한 경우의 수는 아래와 같다.

result = row1*col2 +row2*col1

print(result)
