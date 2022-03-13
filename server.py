from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET



server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000")

def save_note(topic, title, text, str_date_time):
    try:
        tree = ET.parse("db.xml")
        root = tree.getroot()

        topicEle = root.find("topic[@name='{}']".format(topic))
        if topicEle == None:
            topicEle = ET.SubElement(root, "topic", name=topic)
        noteEle = ET.SubElement(topicEle, "note", name=title)
        textEle = ET.SubElement(noteEle, "text")
        textEle.text = text
        str_date_timeEle = ET.SubElement(noteEle, "timestamp")
        str_date_timeEle.text = str_date_time

        tree.write("db.xml")
        print(f"Note {title} created successfully.")
        return True
    except:
        print("Something went wrong.")
        return False

def get_note(topic):
    try:
        tree = ET.parse("db.xml")
        root = tree.getroot()
        notes = []
        topicEle = root.find("topic[@name='{}']".format(topic))
        if topicEle is None:
            print("No notes found")
            return []
        else:
            for note in topicEle.findall("note"):
                title = note.get("name")
                notes.append(title)
                text = note.find("text").text
                notes.append(text)
                str_date_time = note.find("timestamp").text
                notes.append(str_date_time)
            print(f"Found notes for topic {topic}")
            return notes
    except:
        print("Something went wrong.")
        return False


server.register_function(save_note, "save_note")
server.register_function(get_note, "get_note")
server.serve_forever()