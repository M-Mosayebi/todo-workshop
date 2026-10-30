tasks = []


def add_task(title):
    tasks.append({"title": title, "done": False})


def list_tasks():
    for i, t in enumerate(tasks, start=1):
        status = "x" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")


if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Prepare workshop")
    list_tasks()
