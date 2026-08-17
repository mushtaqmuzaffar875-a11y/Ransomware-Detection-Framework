import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from detector import DetectionEngine
from logger import setup_logger


PROJECT_NAME = "Ransomware Detection Framework"
AUTHOR = "MUZAFFAR MUSHTAQ"


class RansomwareEventHandler(FileSystemEventHandler):
    """Connect filesystem events to the detection engine."""

    def __init__(self, detector, logger):
        self.detector = detector
        self.logger = logger

    def _process_file(self, event_type, file_path):
        path = Path(file_path)

        if not path.is_file():
            return

        try:
            result = self.detector.analyze_file(
                path,
                event_type=event_type
            )

            self.logger.info(
                "DETECTION | file=%s | event=%s | "
                "entropy=%.4f | mass_activity=%s | "
                "risk_score=%s | risk_level=%s",
                result["file"],
                result["event_type"],
                result["entropy"],
                result["mass_activity"],
                result["risk_score"],
                result["risk_level"],
            )

            print(
                f"[DETECTION] {event_type.upper():8} | "
                f"Risk: {result['risk_level']:8} | "
                f"Score: {result['risk_score']:3}/100 | "
                f"{path}"
            )

        except (OSError, ValueError) as error:
            self.logger.error(
                "Analysis failed for %s: %s",
                path,
                error
            )

    def on_created(self, event):
        if not event.is_directory:
            self._process_file("created", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self._process_file("modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.logger.info(
                "FILE_EVENT | type=deleted | path=%s",
                event.src_path
            )

    def on_moved(self, event):
        if not event.is_directory:
            self.logger.info(
                "FILE_EVENT | type=moved | from=%s | to=%s",
                event.src_path,
                event.dest_path
            )


def print_banner():
    print("=" * 58)
    print("       RANSOMWARE DETECTION FRAMEWORK")
    print("=" * 58)
    print("       Developed by: MUZAFFAR MUSHTAQ")
    print("=" * 58)
    print()


def main():
    print_banner()

    logger = setup_logger()

    watch_path = Path("data").resolve()

    detector = DetectionEngine(
        entropy_threshold=7.5,
        activity_threshold=20,
        time_window=10,
    )

    handler = RansomwareEventHandler(
        detector,
        logger
    )

    observer = Observer()

    observer.schedule(
        handler,
        str(watch_path),
        recursive=True
    )

    observer.start()

    logger.info(
        "%s started | author=%s | monitoring=%s",
        PROJECT_NAME,
        AUTHOR,
        watch_path
    )

    print(f"[+] Monitoring: {watch_path}")
    print("[+] Detection engine: ACTIVE")
    print("[+] Logging: ACTIVE")
    print("[+] Press Ctrl+C to stop.")
    print()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[+] Stopping framework...")
        observer.stop()

    observer.join()

    logger.info("%s stopped", PROJECT_NAME)
    print("[+] Framework stopped.")


if __name__ == "__main__":
    main()
