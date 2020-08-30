
import xml.etree.ElementTree as ET

tag_column_length = 5
field_name_column_length = 23
trailing_column_length = 50
msg_separator_length = 100

data_dictionary_file = "data-dictionary.xml"
input_file_name = "input.txt"
output_file_name = "output.txt"

print_enums = True

row_char = "-"

tag_dictionary = {}

def build_row_separator():
    global row_separator
    global msg_separator
    row_separator = ""
    for i in range(tag_column_length):
        row_separator += row_char
    row_separator += "-+-"
    for i in range(field_name_column_length):
        row_separator += row_char
    row_separator += "-+-"
    for i in range(trailing_column_length):
        row_separator += row_char
    row_separator += "\n"
    msg_separator = ""
    for i in range(msg_separator_length):
        msg_separator += "#"
    msg_separator += "\n"



def populate_tag_dictionary():
    tree = ET.parse(data_dictionary_file)
    root = tree.getroot()

    for child in root:
        if child.tag == "fields":
            fields = child
    for field in fields:
        tag_dictionary[field.get("number")] = field.get("name")

def make_readable(tags, output_file):
    output_file.write(row_separator)

    for tag in tags:
        pair = tag.split("=")
        if len(pair) == 1:
            continue

        padding1_len = tag_column_length - len(pair[0])
        padding1 = ""

        padding2_len = field_name_column_length - len(tag_dictionary[pair[0]])
        padding2 = ""

        if padding1_len > 0:
            for i in range(padding1_len):
                padding1 = padding1 + " "

        if padding2_len > 0:
            for i in range(padding2_len):
                padding2 = padding2 + " "

        line = pair[0] + padding1 + " | " + tag_dictionary[pair[0]] + padding2 + " | " + pair [1] + "\n"
        output_file.write(line)
        output_file.write(row_separator)


def parse_input_file():
    input_file = open(input_file_name, "r")
    line = input_file.readline()
    output_file = open(output_file_name,"w")

    while line:
        line = line.strip()
        if line == "" or line[0] == "#":
            line = input_file.readline()
            continue
        tags = line.split("|")
        make_readable(tags, output_file)
        output_file.write(msg_separator)
        line = input_file.readline()

    output_file.close()


def main():
    build_row_separator()
    populate_tag_dictionary()
    parse_input_file()


if __name__ == "__main__":
    main()