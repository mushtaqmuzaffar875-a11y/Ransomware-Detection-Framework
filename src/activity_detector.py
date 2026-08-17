from collections import deque
from datetime import datetime, timedelta


class ActivityDetector:
    """Detect unusually high file activity within a time window."""

    def __init__(self, threshold=20, window_seconds=10):
        self.threshold = threshold
        self.window = timedelta(seconds=window_seconds)
        self.events = deque()

    def record_event(self, event_type, path):
        now = datetime.now()

        self.events.append({
            "time": now,
            "type": event_type,
            "path": str(path),
        })

        self._remove_old_events(now)

        return self.analyze()

    def _remove_old_events(self, now):
        while self.events:
            age = now - self.events[0]["time"]

            if age <= self.window:
                break

            self.events.popleft()

    def analyze(self):
        event_count = len(self.events)

        unique_files = len({
            event["path"]
            for event in self.events
        })

        suspicious = unique_files >= self.threshold

        return {
            "events": event_count,
            "unique_files": unique_files,
            "threshold": self.threshold,
            "suspicious": suspicious,
        }


if __name__ == "__main__":
    detector = ActivityDetector(
        threshold=5,
        window_seconds=10
    )

    print("----- ACTIVITY DETECTOR TEST -----")

    for number in range(1, 6):
        result = detector.record_event(
            "modified",
            f"data/test_{number}.txt"
        )

        print(
            f"Event {number}: "
            f"unique_files={result['unique_files']} | "
            f"suspicious={result['suspicious']}"
        )
