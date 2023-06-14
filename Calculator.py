class Addition:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2

#multiplication
def multiply(num1, num2):
    result = 0
    for i in range(num2):
        result = Addition.add(result, num1)

    return(result)

#Subtraction 8-4 =4
def subtract(num1, num2):
            return(Addition.add(num1, (-num2)))

#Division 8 // 4 = 2
def division(num1, num2):
        count = 0
        result = num1 
        while result > 0:
             result = (Addition.add(result, (-num2)))
             if result >= 0:
                   count = Addition.add(count, 1)
        
        return count


value = division(5,10)
print(value)
print ( 5//10)