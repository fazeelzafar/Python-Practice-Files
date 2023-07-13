import threading
import time

# This function will be executed by each thread
def thread_task(message, delay):
    print("Thread started:", threading.current_thread().name)
    print("Message:", message)
    time.sleep(delay)
    print("Thread finished:", threading.current_thread().name)

# A list of tasks
tasks = [
    ("Task 1", 2),
    ("Task 2", 4),
    ("Task 3", 1)
]

# This block of code creates a thread and starts it for each task in the list above
threads = []
for i, (message, delay) in enumerate(tasks):
    thread = threading.Thread(target=thread_task, args=(message, delay), name=f"Thread-{i+1}")
    thread.start()
    threads.append(thread)

# Wait for all threads to complete execution
for thread in threads:
    thread.join()

print("Execution Finished By All Threads")