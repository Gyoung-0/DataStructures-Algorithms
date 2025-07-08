class Record:
    def __init__(self, car_num: int, use_time: int):
        self.car_num = car_num
        self.use_time = use_time
        self.__fee = 0

    def setFee(self, fee: int):
        self.__fee += fee

    def getFee(self) -> int:
        return self.__fee
    
class Bill_Fee:
    @staticmethod
    def get_bill_fee(name: str, hour: int):
        record = Record(name, hour)

        Bill.calculate_fee(record)
        Fee.calculate_fee_another(record)

        return record.getFee()

class Bill:
    @staticmethod
    def calculate_fee(record: Record):
        default_money = 1000
        record.set_fee(default_money * record.use_time)

class Fee:
    @staticmethod
    def calculate_fee_another(record: Record):
        default_money = 5000
        record.setFee(default_money * record.use_time)