from pathlib import Path

try:
    from .entropy_analyzer import EntropyAnalyzer
    from .activity_detector import ActivityDetector
    from .risk_engine import RiskEngine
    from .extension_detector import ExtensionDetector
except ImportError:
    from entropy_analyzer import EntropyAnalyzer
    from activity_detector import ActivityDetector
    from risk_engine import RiskEngine
    from extension_detector import ExtensionDetector


class DetectionEngine:
    """Combine multiple ransomware detection signals."""

    def __init__(
        self,
        entropy_threshold=7.5,
        activity_threshold=20,
        time_window=10,
    ):
        self.entropy_analyzer = EntropyAnalyzer(
            threshold=entropy_threshold
        )

        self.activity_detector = ActivityDetector(
            threshold=activity_threshold,
            window_seconds=time_window,
        )

        self.extension_detector = ExtensionDetector()
        self.risk_engine = RiskEngine()

    def analyze_file(self, file_path, event_type="modified"):
        path = Path(file_path)

        if not path.is_file():
            return {
                "file": str(path),
                "error": "File does not exist",
            }

        # Record file activity
        activity = self.activity_detector.record_event(
            event_type,
            path,
        )

        # Analyze file entropy
        entropy = self.entropy_analyzer.analyze(path)

        # Analyze file extension
        extension = self.extension_detector.analyze(path)

        # Calculate combined risk
        score = self.risk_engine.calculate_score(
            mass_file_activity=activity["suspicious"],
            high_entropy=entropy["high_entropy"],
            suspicious_extension=extension["suspicious"],
        )

        risk_level = self.risk_engine.get_risk_level(score)

        return {
            "file": str(path),
            "event_type": event_type,
            "entropy": entropy["entropy"],
            "high_entropy": entropy["high_entropy"],
            "unique_files": activity["unique_files"],
            "mass_activity": activity["suspicious"],
            "extension": extension["extension"],
            "suspicious_extension": extension["suspicious"],
            "risk_score": score,
            "risk_level": risk_level,
        }


if __name__ == "__main__":
    print("----- DETECTION ENGINE TEST -----")

    detector = DetectionEngine()

    test_file = Path("data/detection_test.txt")
    test_file.write_text(
        "Safe ransomware detection framework test.",
        encoding="utf-8",
    )

    result = detector.analyze_file(
        test_file,
        event_type="modified",
    )

    for key, value in result.items():
        print(f"{key}: {value}")
