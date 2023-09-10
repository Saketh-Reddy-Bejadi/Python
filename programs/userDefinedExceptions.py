class CustomException(Exception):
    pass

def process_data(data):
    if data is None:
        raise CustomException("Invalid data.")

try:
    a=input("Enter:")
    process_data(a)
except CustomException as e:
    print("Error:", str(e))
