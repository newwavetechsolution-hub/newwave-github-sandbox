"""Simple CLI that uses backend."""
from backend.greet import greet

def main():
    print(greet("User"))

if __name__ == "__main__":
    main()
