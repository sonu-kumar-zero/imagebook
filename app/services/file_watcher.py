from PySide6.QtCore import QObject, Signal
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class WatcherHandler(FileSystemEventHandler):

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def on_modified(self, event):
        if not event.is_directory:
            self.callback(event.src_path)


class FileWatcher(QObject):

    file_changed = Signal(str)

    def __init__(self, path):
        super().__init__()

        self.path = path

        self.observer = Observer()

        self.handler = WatcherHandler(
            self.emit_change
        )

    def emit_change(self, path):
        self.file_changed.emit(path)

    def start(self):
        self.observer.schedule(
            self.handler,
            self.path,
            recursive=True
        )

        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()