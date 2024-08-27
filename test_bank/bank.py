def main():
    user_input = input("Greeting: ").strip().lower()
    greeting(user_input)

def greeting(user: str):
    if "hello" in user:
        print("$0")
    elif user.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
