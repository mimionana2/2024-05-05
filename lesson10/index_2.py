import pyinputplus as pyip
import healthy


def main():
    name:str=input("請輸入姓名:")
    print(f"請輸入姓名:{name}")

    height:int=pypi.inputInt("請輸入身高cm:")
    print (hight)
    weight:int=pypi.inputInt("請輸入體重kg:")
    print (weight)

    bmi:float=cal_bmi(height,weight)
    print(f"您的bmi值:{round(bmi,ndigits=2)}")
    print(f"您的身體質量指數:{get_status(bmi)}")
