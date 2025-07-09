class Bill:
    @staticmethod
    def get_bill_fee(time:int, discount:int):
        discount_percentage = discount / 100
        # 메서드 안에 또 다른 메소드를 호출해 의존도가 있긴 하지만, 메소드에 단순 파라미터 데이터를 보내는 형태
        return Fee.calculate_fee(time) * discount_percentage
    
class Fee:
    @staticmethod
    def calculate_fee(time: int):
        defaultMoney = 1000
        return defaultMoney * time
    
if __name__ == "__main__":
    Bill.get_bill_fee(2,80)