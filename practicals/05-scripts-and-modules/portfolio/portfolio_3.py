if __name__ == "__main__":
    import sys
    def arguments(*kwargs):

        if len(sys.argv) > 1:
            args = sys.argv[1:]
            args.sort(key=len)

            shortest = args[0]
            print("Shortest argument value:", shortest)

        else:
            print("no args were passed...")

arguments()