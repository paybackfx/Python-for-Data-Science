import sys
from ft_filter import ft_filter

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        n = int(sys.argv[2])

        words = s.split()
        result = ft_filter(lambda w: len(w) > n, words)
        print(result)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()
