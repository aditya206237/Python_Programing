class InvalidNumberError(Exception):
    def __init__(self,no,message="Please Enter A Positive number.."):
        self.no=no
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message}. Provided Number: {self.no}"
    
def set__no(no):
    if no<0:
        raise InvalidNumberError(no)
    elif no==0:
        print("Number is equals to zero..")
    else:
        print(f"Number is positive {no}") 
no=int(input("Enter a number:-"))
try:
    set__no(no)
except InvalidNumberError as e:
    print(f"Negative Number: {e.no}. {e.message}")  