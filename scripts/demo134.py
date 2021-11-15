import sys
import getopt
import demo123

if __name__=="__main__":
    print("calling main")
    # arg = sys.argv[1:]
    opts,args = getopt.getopt(sys.argv[1:],"",["number=","loglevel="])
    # print(arg)
    for o,a in opts:
        print(o,a)

    demo123.add("number1:2 number2:3")