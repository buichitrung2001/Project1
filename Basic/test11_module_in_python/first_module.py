print("Import successfully")
print(f"First_module's name: {__name__}")

def plus(a, b):
    return a + b

#nên tách thành hàm main để có thể gọi hàm main ở second_module
def main(): 
    return "This is the main function of the first module"

if __name__ == "__main__":
    main()