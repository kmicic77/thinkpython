""" checking Fermat's theorem"""

def check_fermat(a,b,c,n):
    if n>2 and a**n+b**n==c**n:
	    print("Holy smokes! Fermat was wrong!")
    else:
	    print("No, that doesn't work.")
def ask_for_input():
    a=int(input("Give me \"a\": "))
    b=int(input("Give me \"b\": "))
    c=int(input("Give me \"c\": "))
    n=int(input("Give me \"n\": "))
    check_fermat(a,b,c,n)
ask_for_input()

