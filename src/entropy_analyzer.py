from pathlib import Path
import math
from collections import Counter


class EntropyAnalyzer:
    """Calculate Shannon entropy for files."""

    def __init__(self, threshold=7.5):
        self.threshold = threshold

    def calculate_entropy(self, file_path):
        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")

        data = path.read_bytes()

        if not data:
            return 0.0

        frequencies = Counter(data)
        length = len(data)

        entropy = 0.0

        for count in frequencies.values():
            probability = count / length
            entropy -= probability * math.log2(probability)

        return entropy

    def analyze(self, file_path):
        entropy = self.calculate_entropy(file_path)

        return {
            "file": str(file_path),
            "entropy": round(entropy, 4),
            "threshold": self.threshold,
            "high_entropy": entropy >= self.threshold,
        }


if __name__ == "__main__":
    analyzer = EntropyAnalyzer()

    test_file = Path("data/entropy_test.txt")
    test_file.write_text(
        "This is a safe entropy analysis test file.\n" * 100,
        encoding="utf-8"
    )

    result = analyzer.analyze(test_file)

    print("----- ENTROPY ANALYSIS -----")
    print(f"File: {result['file']}")
    print(f"Entropy: {result['entropy']}")
    print(f"Threshold: {result['threshold']}")
    print(f"High Entropy: {result['high_entropy']}")

    test_file.unlink()
