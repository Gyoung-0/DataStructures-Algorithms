class Bill:
    @staticmethod
    def get_bill_fee(time: int, discount: int, fee_calulator):
        discount_percnetage = discount / 100
        return fee_calulator(time) * discount_percnetage
    
class Fee:
    @staticmethod
    def calculate_fee(time: int):
        return 1000 * time
    
if __name__ == "__main__":
    result = Bill.get_bill_fee(2, 80, Fee.calculate_fee)
    print(result)