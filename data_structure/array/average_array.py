from sum_array import sum_array

def average_array(arr):
    if not arr:
        return None
    
    numbers = [x for x in arr if isinstance(x, (int, float))]
    if not numbers:
        raise ValueError("입력된 리스트에 숫자가 없습니다.")
    
    return sum_array(numbers) / len(numbers)