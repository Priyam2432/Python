def greet(fx):
    def mfx():
        fx()
        print("Good moring")
        return mfx


@greet
def check():
    print("Hello World !")
check()
    