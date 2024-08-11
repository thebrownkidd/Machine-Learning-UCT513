from topsis.topsis import run
import sys as s
if __name__ == "__main__":
    print("Converting said file")
    # print(s.argv)
    run(str(s.argv[1]),s.argv[3],s.argv[2],s.argv[4])