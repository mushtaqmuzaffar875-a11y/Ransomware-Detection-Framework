import time
from pathlib import Path


TEST_DIR = Path("data/simulator_test")


def create_test_files(count=5):
    TEST_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[+] Creating {count} safe test files...")

    for number in range(1, count + 1):
        file_path = TEST_DIR / f"test_document_{number}.txt"

        file_path.write_text(
            f"Safe ransomware detection test file {number}\n",
            encoding="utf-8",
        )

        print(f"[CREATED] {file_path}")
        time.sleep(0.3)


def modify_test_files():
    print("[+] Modifying test files...")

    for file_path in sorted(TEST_DIR.glob("*.txt")):
        with file_path.open("a", encoding="utf-8") as file:
            file.write("Safe simulated activity.\n")

        print(f"[MODIFIED] {file_path}")
        time.sleep(0.3)


def main():
    print("=" * 55)
    print("       SAFE ACTIVITY SIMULATOR")
    print("       MUZAFFAR MUSHTAQ")
    print("=" * 55)

    create_test_files()
    modify_test_files()

    print("[+] Safe simulation completed.")
    print(f"[+] Test directory: {TEST_DIR}")


if __name__ == "__main__":
    main()
