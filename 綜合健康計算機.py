#綜合健康計算機(BMI,BMR,TDEE)

print("歡迎使用綜合健康計算機～")
print("(1)計算BMI")
print("(2)計算BMR")
print("(1)計算TDEE")
#計算BMI函式
def get_bmi(height,weight):
    height = height / 100
    bmi = weight /height ** 2
    bmi = round(bmi,2)
    return bmi
#計算BMR函式
def get_bmr(sex,height,weight,age):
    if sex == "女":
        bmr = 655 + (9.6*weight + 1.8*height - 4.7*age)
        return bmr
    else:
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
        bmr = round(bmr,2)
        return bmr
#計算TDEE函式
def get_tdee(sex,height,weight,age,time):
    if time == 1:
        tdee = get_bmr(sex,height,weight,age)*1.2
        return tdee
    elif time == 2:
        tdee = get_bmr(sex,height,weight,age)*1.375
        return tdee
    elif time == 3:
        tdee = get_bmr(sex,height,weight,age)*1.55
        return tdee
    elif time == 4:
        tdee = get_bmr(sex,height,weight,age)*1.725
        return tdee
    else:
        tdee = get_bmr(sex,height,weight,age)*1.9
        return tdee

a = input("請選擇要計算的項目(輸入1或2或3)\n")
if a == "1":
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    print(f"您的BMI為{get_bmi(height,weight)}")
elif a == "2":
    sex = (input("請輸入您的性別(男或女)"))
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    age = int(input("請輸入您的年紀"))
    print(f"您的基礎代謝率(BMR)為{get_bmr(sex, height, weight, age)}")
else:
    sex = (input("請輸入您的性別(男或女)"))
    height = float(input("請輸入您的身高(公分)"))
    weight = float(input("請輸入您的體重(公斤)"))
    age = int(input("請輸入您的年紀"))
    print("(1)久坐，幾乎沒運動")
    print("(2)每週低強度運動1-3天")
    print("(3)每週中強度運動3-5天")
    print("(4)每週高強度運動6-7天")
    print("(5)勞力密集工作或是每天高強度訓練")
    time = input("請輸入您的運動量(1-5)")
    print(f"您的總熱量消耗(TDEE)：{get_tdee(sex, height, weight, age, time)}")
