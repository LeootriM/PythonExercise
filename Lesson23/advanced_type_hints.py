from typing import Optional, Any
from typing import List
from typing import Union

'''Optional example '''

def get_name(name:Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name("j"))

'''Union example'''
def process_value(value: Union[int,str]) ->str:
    if isinstance(value, int):
        return f"Number: {value}"
    return  f"String: {value}"
print(process_value("ds"))

'''Any example '''

def process_anything(value:Any):
    return f"Processed {value}"

print(process_anything("hah"))

def sum_list(number: List[int]) ->int:
    return sum(number)

numbers: List[int] = [1,2,3,4,5]
result: int = sum_list(numbers)
print(result)