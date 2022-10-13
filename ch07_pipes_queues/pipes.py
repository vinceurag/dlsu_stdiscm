import multiprocessing

def send_function(conn, messages):
    for msg in messages:
        conn.send(msg)
        print(f"{multiprocessing.current_process().name} sends the message: {msg}")

def receive_function(conn):
    while True:
        msg = conn.recv()
        print(f"{multiprocessing.current_process().name} received the message: {msg}")
        if msg == "halt":
            break


def run():
    messages = ["Hello", "World", "How are you?", "halt"]
    sender_conn, receiver_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=send_function, args=(sender_conn, messages))
    p2 = multiprocessing.Process(target=receive_function, args=(receiver_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    run()
