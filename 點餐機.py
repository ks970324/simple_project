#拉麵點餐系統
print("歡迎使用拉麵點餐機～")
print("(1)鹽味拉麵 220")
print("(2)醬油拉麵 240")
print("(3)豚骨拉麵 280")
order = input("請選擇拉麵口味(輸入1 or 2 or 3)")
#upper 將字母變大寫 , lower 將字母變小寫
#+lower改善使用者填寫到大寫修正程式誤判為不加的問題
big = input("是否加大？豚骨口味+$50,其他口味+$30(輸入y或n)").lower()
egg = input("是否加溏心蛋+$30(輸入y或n)").lower()
meat =input("是否加叉燒+$60(輸入y或n)").lower()
#依序將bill做計算即可，填寫input裡面是字串，因此if下 =="口味"
bill = 0
if order == "1":
    bill += 220
elif order == "2":
    bill+= 240
else:
    bill += 280
if big == "y":
    if order == "3":
        bill += 50
    else:
        bill += 30

if egg == "y":
    bill += 30

if meat == "y":
    bill += 60
#3個皆加有折價
#/n空行

if big == "y" and egg == "y" and meat == "y":
    bill -= 20
    print(f"\n\n配料皆加折扣$20，總金額${bill}，感謝您的光臨!")
else:
    print(f"\n\n總金額${bill}，感謝您的光臨!")