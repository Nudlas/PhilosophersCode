import threading
import time
import random

# Initialize fork locks
fork_0 = threading.Lock()
fork_1 = threading.Lock()

# Number of times each philosopher will eat
EAT_TIMES = 5

def philosopher(phil_id):
    left_fork = fork_0 if phil_id == 0 else fork_1
    right_fork = fork_1 if phil_id == 0 else fork_0

    for i in range(EAT_TIMES):
        # Thinking
        print(f"Philosopher {phil_id} is thinking 🤔")
        time.sleep(random.uniform(0.5, 1.5))

        print(f"Philosopher {phil_id} is hungry 😋")

        # Deadlock-avoiding strategy
        if phil_id == 0:
            with left_fork:
                print(f"Philosopher {phil_id} picked up left fork 🥢")
                with right_fork:
                    print(f"Philosopher {phil_id} picked up right fork 🍴 — eating now")
                    time.sleep(random.uniform(0.5, 1.0))
                    print(f"Philosopher {phil_id} finished eating 🧘")
        else:
            with right_fork:
                print(f"Philosopher {phil_id} picked up right fork 🥢")
                with left_fork:
                    print(f"Philosopher {phil_id} picked up left fork 🍴 — eating now")
                    time.sleep(random.uniform(0.5, 1.0))
                    print(f"Philosopher {phil_id} finished eating 🧘")

    print(f"Philosopher {phil_id} is done with meals 🚶‍♂️")

# Launch philosopher threads
t0 = threading.Thread(target=philosopher, args=(0,))
t1 = threading.Thread(target=philosopher, args=(1,))

t0.start()
t1.start()

t0.join()
t1.join()

print("🍽️ All philosophers are done dining.")
