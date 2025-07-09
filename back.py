
class Backend():

    def save_to_file(self, file_name, data):
        with open(file_name, "w+") as text_file:
            print(data, file=text_file)

    def read_from_file(self, file_name):
        with open(file_name,"r") as text_file:
            return text_file.read()