import xmlrpc.client
import sys
from datetime import datetime
try:
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")



    def menu():
        print("1) Enter a new note")
        print("2) Get note")
        print("0) Exit")
        choice = input("Your choice:")
        return int(choice)

    while True:
        choice = menu()
        if choice == 1:
            print("\n")
            topic = input("What is the topic: ")
            title = input("What is the title: ")
            text = input("Enter your text: ")
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            date_time = datetime.fromtimestamp(ts)
            str_date_time = date_time.strftime("%d/%m/%Y - %H:%M:%S")
            print("\n")
            proxy.save_note(topic, title, text, str_date_time)
        elif choice == 2:
             topic = input("What topic are you looking for: ")
             notes = proxy.get_note(topic)
             if (len(notes) == 0):
                 print(f"No notes found with {topic} topic.")
                 print("\n")
             else:
                 print(notes)
                 print("\n")
        elif choice == 0:
            sys.exit(0)
        else:
            print("Invalid choice. Try again.\n")
    menu()

except Exception as err:
        print(err)
        input()
