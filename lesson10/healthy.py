class Bmi():
    def __init__(self,n:str): #自訂的init
        self.name = n

    def __repr__(self) -> str:
        return f'我的名字叫{self.name}'

class Bmi:
    def __init__(self,n:str,h:int,w:int):
        super().__init__(n) #執行父類別的init
        self.__hight = h
        self.__weight =g


    @property
    def name(self)-> int:
        return self.__name

    @property
    def hight(self)-> int:
        return self.__hight
    
    @property
    def weight(self) -> int:
        return self.__weight
    
    
    @classmethod
    def cal_bmi(cls,height:int,weight:int) -> float:
        bmi = weight/(hight/100)**2
        return Bmi
    
    @classmethod
    def get_status(bmi:float)->str:

        if  bmi<18.5:
            return "過輕"
        elif bmi<24:
            return "正常" 
        elif bmi<27:
            return "過重"
        elif bmi<30:
            return "輕度肥胖"
        elif bmi<35:
            return "中度肥胖"
        else:
            return "重度肥胖"

