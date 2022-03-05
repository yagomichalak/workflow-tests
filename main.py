import os
from dotenv import load_dotenv
load_dotenv()

random_var: int = int(os.getenv('RANDOM_VAR'))

def main() -> None:
    print(f"This is a random var: {random_var}")


if __name__ == '__main__':
    main()