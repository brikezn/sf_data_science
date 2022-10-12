import numpy as np

def random_predict(number:int=1) -> int:
    """Угадывание случайного числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    start_index  = 0
    end_index = 100
    
    while True:
        count += 1
        medium_index =  start_index + (end_index - start_index) / 2
        predict_number = int(medium_index)
        
        
        if predict_number > number:
            end_index = int(medium_index)
        elif predict_number < number:
            start_index = int(medium_index)
        else:
            break
        
        
    return count
        
print(f'Количество попыток: {random_predict(10)}')
