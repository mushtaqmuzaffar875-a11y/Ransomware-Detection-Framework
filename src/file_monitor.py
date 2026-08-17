import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileActivityHandler(FileSystemEventHandler):
    """Handles filesystem activity events."""

    def _log_event(self, event_type, path):
        if event_type == "directory":
            return

        logging.info(
            "FILE_EVENT | type=%s | path=%s",
            event_type,
            path
        )

        print(f"[FILE EVENT] {event_type.upper():8} | {path}")

    def on_created(self, event):
        self._log_event("created", event.src_path)

    def on_modified(self, event):
        self._log_event("modified", event.src_path)

    def on_deleted(self, event):
        self._log_event("deleted", event.src_path)

    def on_moved(self, event):
        self._log_event(
            "moved",
            f"{event.src_path} -> {event.dest_path}"
        )


class FileMonitor:
    """Monitors filesystem activity in a directory."""

    def __init__(self, watch_path, recursive=True):
        self.watch_path = Path(watch_path).resolve()
        self.recursive = recursive
        self.observer = Observer()

    def start(self):
        if not self.watch_path.exists():
            raise FileNotFoundError(
                f"Monitoring path does not exist: {self.watch_path}"
            )

        if not self.watch_path.is_dir():
            raise NotADirectoryError(
                f"Monitoring path is not a directory: {self.watch_path}"
            )

        handler = FileActivityHandler()

        self.observer.schedule(
            handler,
            str(self.watch_path),
            recursive=self.recursive
        )

        self.observer.start()

        print(f"[+] Monitoring: {self.watch_path}")
        print("[+] Press Ctrl+C to stop.")

        try:
            while self.observer.is_alive():
                self.observer.join(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("\n[+] File monitor stopped.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    monitor = FileMonitor("data")
    monitor.start()
