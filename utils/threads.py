""" Defines all thread classes. """

from collections import defaultdict
from collections.abc import Callable
from threading import Thread, Event
import queue
import customtkinter as ctk
from utils.observer_publisher import progress_publisher
from utils.scrollable_frame_manager import ScrollableFrameManager
from models.csv_data_manager import csv_data_manager


class UpdateWidgetThread(Thread):
    """
    Handle the updating of the scrollable frame.
    """

    __slots__ = (
        "daemon",
        "event",
        "__scrollable_frame_manager",
        "__header_list",
        "__header_seperator",
    )

    def __init__(
        self,
        header_scrollableframe: ctk.CTkScrollableFrame,
        header_list: defaultdict[str, list[int] | list[tuple[str, int]]],
        header_seperator: str,
    ) -> None:
        super().__init__()

        self.daemon = True
        self.event = Event()

        self.__scrollable_frame_manager: ScrollableFrameManager = header_scrollableframe

        self.__header_list: defaultdict[str, list[int] | list[tuple[str, int]]] = (
            header_list
        )
        self.__header_seperator: str = header_seperator

    def run(self) -> None:
        self.__scrollable_frame_manager.update_scrollable_frame(
            self.__header_list,
            self.__header_seperator,
            csv_data_manager.get_raw_data_columns_count(),
        )
        progress_publisher.progress_mode = "stop"
        self.event.set()


class SafeThread(Thread):
    """
    This class allows safe multi-threading by running a function in a background thread,
    while also executing functions before the thread starts and after it finishes.
    It includes a mechanism to check if the thread is currently running.
    """

    def __init__(
        self,
        *thread_args: any,
        target: Callable[..., any] | None = None,
        args: tuple[any, ...] = (),
        before_thread: Callable[[], None] | None = None,
        after_thread: Callable[[], None] | None = None,
        **thread_kwargs: any
    ) -> None:
        """
        Initializes the SafeThread object.

        Args:
            target (Callable[..., any] | None, optional): The function to run in the thread. Defaults to None.
            args (tuple[any, ...], optional): The arguments to pass to the target function. Defaults to ().
            before_thread (Callable[[], None] | None, optional):  A function to execute before the thread starts. Defaults to None.
            after_thread (Callable[[], None] | None, optional): A function to execute after the thread finishes. Defaults to None.
        """
        super().__init__(*thread_args, **thread_kwargs)

        self.daemon = True  # To automatically terminate thread when program exits

        # The function to be run in the thread
        self.target: Callable[..., any] | None = target
        # Arguments for the target function
        self.args: tuple[any, ...] = args

        # Function to execute before the thread starts
        self.before_thread = before_thread

        # Function to execute after the thread finishes
        self.after_thread = after_thread

        # Flag to indicate if the thread is currently running
        self._is_running: bool = False

    def run(self) -> None:
        """
        Overrides the run method of Thread. Executes the before_thread function (if provided),
        then runs the target function with the specified arguments, and finally executes the
        after_thread function (if provided). Updates the internal _is_running flag accordingly
        """
        self._is_running = True  # Mark the thread as running

        # Execute the before_thread function if provided
        if self.before_thread:
            self.before_thread()

        # Run the actual target function
        if self.target:
            self.target(*self.args)

        # Execute the after_thread function if provided
        if self.after_thread:
            self.after_thread()

        self._is_running = False  # Mark the thread as finished

    def is_running(self) -> bool:
        """
        Checks if the thread is currently running

        Returns:
            bool: True if the thread is running, False otherwise.
        """
        return self._is_running  # Return the running state of the thread


class SafeThreadQueue:
    """
    SafeThreadQueue manages a queue of SafeThread objects that are executed sequentially
    by a worker thread. Each SafeThread can have a function that is executed before the
    thread starts and after it finishes.
    """

    def __init__(self) -> None:
        """
        Initializes the SafeThreadQueue with a task queue and starts a worker thread.
        """
        self.task_queue = queue.Queue()  # Queue to hold SafeThread objects
        self.worker_thread = Thread(target=self.worker, daemon=True)  # Worker thread
        self.worker_thread.start()  # Start the worker thread

    def worker(self) -> None:
        """
        The worker function that runs in the worker thread. It continuously fetches
        and executes SafeThread tasks from the queue.
        """
        while True:
            task = self.task_queue.get()  # Get a SafeThread task from the queue

            if task is None:  # Sentinel value to stop the worker
                break

            task.start()  # Start the SafeThread
            task.join()  # Wait for the SafeThread to finish
            self.task_queue.task_done()  # Mark the task as done

    def add_task(
        self,
        target: Callable[..., any],
        args: tuple[any, ...] = (),
        before_thread: Callable[[], None] | None = None,
        after_thread: Callable[[], None] | None = None,
    ) -> None:
        """
        Adds a new SafeThread task to the queue.

        Args:
            target (Callable[..., any]): The function to be executed by the SafeThread
            args (tuple[any, ...], optional): The arguments to pass to the target function. Defaults to ().
            before_thread (Callable[[], None] | None, optional):  A function to execute before the thread starts. Defaults to None.
            after_thread (Callable[[], None] | None, optional): A function to execute after the thread finishes. Defaults to None.
        """
        task = SafeThread(
            target=target,
            args=args,
            before_thread=before_thread,
            after_thread=after_thread,
        )
        self.task_queue.put(task)  # Add the SafeThread task to the queue

    def stop_worker(self) -> None:
        """
        Stops the worker thread by adding a sentinel value (None) to the queue.
        This tells the worker to stop processing tasks.
        """
        self.task_queue.put(None)  # Add sentinel to stop the worker
        self.worker_thread.join()  # Wait for the worker thread to finish


safe_thread_queue = SafeThreadQueue()
