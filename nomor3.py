import sys

if __name__ == "__main__":
    max_num = 9
    if (len(sys.argv)>1 and sys.argv[1].isdigit()) and int(sys.argv[1])>0 :
        max_num = int(sys.argv[1])        

    def print_next(a=0, b=0, i=0, string=""):
        c = a + b
        if (i == 0):
            string = str(c)
            b = 1
        else: 
            string += ", " + str(c)
        i += 1
        if (i>=max_num):
            print(string)
            return
        print_next(b,c,i,string)

    print(f"print {max_num} number ")
    print_next()