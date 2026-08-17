from pathlib import Path


class ExtensionDetector:
    """Detect potentially suspicious file extensions."""

    def __init__(self):
        self.suspicious_extensions = {
            ".encrypted",
            ".locked",
            ".crypt",
            ".enc",
            ".ransom",
        }

    def analyze(self, file_path):
        path = Path(file_path)

        extension = path.suffix.lower()

        suspicious = extension in self.suspicious_extensions

        return {
            "file": str(path),
            "extension": extension,
            "suspicious": suspicious,
        }


if __name__ == "__main__":
    detector = ExtensionDetector()

    test_files = [
        "document.txt",
        "important.locked",
        "backup.encrypted",
    ]

    print("----- EXTENSION DETECTOR TEST -----")

    for file_name in test_files:
        result = detector.analyze(file_name)

        print(
            f"{result['file']} | "
            f"extension={result['extension']} | "
            f"suspicious={result['suspicious']}"
        )
