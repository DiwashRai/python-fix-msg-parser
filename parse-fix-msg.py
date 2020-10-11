
import argparse
import sys
import xml.etree.ElementTree as ET


class FIXParser:
    tag_column_length = 5
    field_name_column_length = 23
    trailing_column_length = 65
    msg_separator_length = 100


    def __init__(self):
        parser = argparse.ArgumentParser(description=("Parse FIX messages from a text file against a Data Dictionary and output them with field names and enum information."))
        parser.add_argument("--input", action="store", dest="input", help="input text file path.")
        parser.add_argument("--output", action="store", dest="output", help="output text file path.")
        parser.add_argument("--data_dictionary", "--dd", action="store", dest="data_dictionary", help="data dictionary xml file path.")
        parser.add_argument("--hide_enums", action="store_true", help="lists all possible enums in a row if field is of type enum.")
        parser.add_argument("--row_lines", action="store_true", help="separates each row with lines for visual clarity.")
        self.args = parser.parse_args()

        if self.args.input == "" or self.args.input is None:
            print("Error: specify input file path with --input")
            sys.exit(1)

        if self.args.output == "" or self.args.output is None:
            print("Error: specify output file path with --output")
            sys.exit(1)

        if self.args.data_dictionary == "" or self.args.data_dictionary is None:
            print("Error: specify data dictionary file path with --dd")
            sys.exit(1)


    def build_row_separator(self):
        self.row_separator = ""
        for i in range(self.tag_column_length):
            self.row_separator += "-"
        self.row_separator += "-+-"
        for i in range(self.field_name_column_length):
            self.row_separator += "-"
        self.row_separator += "-+-"
        for i in range(self.trailing_column_length):
            self.row_separator += "-"
        self.row_separator += "\n"


    def build_msg_separator(self):
        self.msg_separator = ""
        for i in range(self.msg_separator_length):
            self.msg_separator += "#"
        self.msg_separator += "\n"


    def init_fields(self):
        tree = ET.parse(self.args.data_dictionary)
        root = tree.getroot()

        for child in root:
            if child.tag == "fields":
                self.fields = child


    def get_enum_str(self, tag_number, tag_value):
        enums = ""
        field = self.fields.find(f"./field[@number='{tag_number}']")

        firstVal = field.find("./value")
        if not firstVal is None:
            meaning = field.find(f"./value[@enum='{tag_value}']")
            if not meaning is None:
                enums += " (" + meaning.get("description") + ")"
            else:
                enums += " (ERROR: NO MATCHING ENUM. CHECK DICTIONARY)"

        if field:
            enum_padding = self.trailing_column_length - len(enums)
            for i in range(enum_padding):
                enums += " "
            for enum in field:
                enums += enum.get("enum") + " : " + enum.get("description") + ", "
        return enums


    def make_readable(self, tags, output_file):
        if self.args.row_lines:
            output_file.write(self.row_separator)

        for tag in tags:
            pair = tag.split("=")
            if len(pair) == 1:
                continue

            tag_number = pair[0]
            tag_name = self.fields.find(f"./field[@number='{tag_number}']").get("name")
            tag_value = pair[1]

            padding1_len = self.tag_column_length - len(tag_number)
            padding1 = ""
            if padding1_len > 0:
                for i in range(padding1_len):
                    padding1 = padding1 + " "

            padding2_len = self.field_name_column_length - len(tag_name)
            padding2 = ""
            if padding2_len > 0:
                for i in range(padding2_len):
                    padding2 = padding2 + " "

            enums = ""
            if not self.args.hide_enums:
                enums = self.get_enum_str(tag_number, tag_value)

            line = tag_number + padding1 + " | " + tag_name + padding2 + " | " + tag_value + enums + "\n"
            output_file.write(line)
            if self.args.row_lines:
                output_file.write(self.row_separator)


    def parse_input_file(self):
        input_file = open(self.args.input, "r")
        line = input_file.readline()
        output_file = open(self.args.output,"w")

        while line:
            line = line.strip()
            if line == "" or line[0] == "#":
                line = input_file.readline()
                continue
            tags = line.split("|")
            self.make_readable(tags, output_file)
            output_file.write(self.msg_separator)
            line = input_file.readline()

        output_file.close()


def main():
    parser = FIXParser()
    parser.build_row_separator()
    parser.build_msg_separator()
    parser.init_fields()
    parser.parse_input_file()


if __name__ == "__main__":
    main()