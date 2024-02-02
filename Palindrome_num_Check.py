x = int(input("Please enter an integer value"))
def isPalindrome(x):
    x = str(x)
    String = ""
    Backward_String = ""
    Valid = False
    for i in range(len(x)):
        String = String + x[i]

    for j in range(len(x),0,-1):
        Backward_String = Backward_String + x[j-1]

    if String == Backward_String:
        Valid = True
    else:
        Valid = False

    return Valid

print("The result of checking whether your number is a palindrome number is:",isPalindrome(x))
#If output is true, this number is a palindrome number.   If the output is false, then it is not a palindrome number
