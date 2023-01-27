#  by Suphinya Wu 

# input น้ำผลไม้ (1 = น้ำส้ม13บาท, 2 = น้ำแอปเปิล15บาท, 3 = น้ำกีวี22บาท)
# input เงินหยอดเหรียญ (a = 1บาท, b = 2บาท, c = 5บาท, d = 10บาท)

# --------------------------- program --------------------------------
# คำนวนค่าเงิน
def cal_mon(money):
    total_money = 0 
    for m in range(len(money)) :
        if money[m] == "a" :
            total_money += 1
        elif money[m] == "b" :
            total_money += 2
        elif money[m] == "c" :
            total_money += 5
        elif money[m] == "d" :
            total_money += 10
    # print(total_money)      # ex a ,, b, c ,d,a,a = 20
    return(total_money)

# รับค่าน้ำผลไม้
juice = input("Please enter the juices number(1,2,3) : ")
juice = juice.replace(",,",",")             # กรณี 1,,2
juice = juice.replace(" ","").split(",")    # กรณี 1 ,2 , 3 ,1

# คำนวนค่าน้ำผลไม้
total_price = 0 
for j in range(len(juice)) :
    if juice[j] == "1" :
        total_price += 13
    elif juice[j] == "2" :
        total_price += 15
    elif juice[j] == "3" :
        total_price += 22
print("total juice price : "+str(total_price))      # ex 1 , 2, 3 ,1 = 63


# รับค่าเงิน
money = input("Please insert your money(a,b,c,d) : ")
money = money.replace(",,",",")             # กรณี a,,b
money = money.replace(" ","").split(",")    # กรณี a ,b , c ,d

total_money = cal_mon(money)
print("total money : "+str(total_money))

a = 0
b = 0
c = 0
d = 0
change = 0

x = True
while(x):   # เงื่อนไขคำนวนกรณีใส่เงินไม่เพียงพอ
    if total_money - total_price < 0 :
        x = input("please insert more money(a,b,c,d) : ")
        x = x.replace(",,",",")             # กรณี a,,b
        x = x.replace(" ","").split(",")    # กรณี a ,b , c ,d
        total_money += cal_mon(x)
        print("total money : "+str(total_money))
    else:
        change = total_money - total_price
        x = False
print("เงินที่ต้องทอน คือ "+str(change)+" บาท")


while(change!=0):    # คำนวนจำนวนเหรียญที่ต้องทอน
    if change-10 >= 0 :
        change -= 10
        d += 1
    elif change-5 >= 0 :
        change -= 5
        c += 1
    elif change-2 >= 0 :
        change -= 2
        b += 1
    elif change-1 >= 0 :
        change -= 1
        a += 1

if a != 0 :
    print("เหรียญ 1 บาท จำนวน : "+str(a)+" เหรียญ")
if b != 0 :
    print("เหรียญ 2 บาท จำนวน : "+str(b)+" เหรียญ")
if c != 0 :
    print("เหรียญ 5 บาท จำนวน : "+str(c)+" เหรียญ")
if d != 0 :
    print("เหรียญ 10 บาท จำนวน : "+str(d)+" เหรียญ")
   