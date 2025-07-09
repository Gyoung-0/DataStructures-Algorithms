class Record:
    def __init__(self, car_num: int, use_time: int):
        self.car_num = car_num
        self.use_time = use_time
        self.__fee = 0

    def set_fee(self, fee: int):
        self.__fee += fee

    def get_fee(self) -> int:
        return self.__fee
    
class Bill:
    def calculate_fee(self, record: Record):
        default_money = 1000
        record.set_fee(default_money * record.use_time)

class DiscountBill(Bill):
    def calculate_fee(self, record: Record):
        default_money = 500
        record.set_fee(default_money * record.use_time)

class Fee:
    def calculate_fee_anoter(self, record: Record):
        default_money = 5000
        record.set_fee(default_money * record.use_time)

class BillFee:
    def __init__(self, bill: Bill, fee: Fee):
        self.bill = bill
        self.fee = fee

    def get_bill_fee(self, car_num, use_time):
        record = Record(car_num, use_time)