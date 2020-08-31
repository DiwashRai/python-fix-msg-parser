
import xml.etree.ElementTree as ET

tag_column_length = 5
field_name_column_length = 23
trailing_column_length = 50
msg_separator_length = 100

data_dictionary_file = "FIX44.xml"
input_file_name = "input.txt"
output_file_name = "output.txt"

print_enums = True
use_row_separators = False

row_char = "-"

def build_row_separators():
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


def init_fields():
    global fields
    tree = ET.parse(data_dictionary_file)
    root = tree.getroot()

    for child in root:
        if child.tag == "fields":
            fields = child


def get_enum_str(tag_number):
    enums = ""
    field = fields.find(f"./field[@number='{tag_number}']")
    enum_padding = len(row_separator) - (tag_column_length + 3 + field_name_column_length + 3 + 1)

    if field:
        for i in range(enum_padding):
            enums += " "
        for enum in field:
            enums += enum.get("enum") + " : " + enum.get("description") + ", "
    return enums


def make_readable(tags, output_file):
    if use_row_separators:
        output_file.write(row_separator)

    for tag in tags:
        pair = tag.split("=")
        if len(pair) == 1:
            continue

        tag_number = pair[0]
        tag_name = fields.find(f"./field[@number='{tag_number}']").get("name")
        tag_value = pair[1]

        padding1_len = tag_column_length - len(tag_number)
        padding1 = ""
        if padding1_len > 0:
            for i in range(padding1_len):
                padding1 = padding1 + " "

        padding2_len = field_name_column_length - len(tag_name)
        padding2 = ""
        if padding2_len > 0:
            for i in range(padding2_len):
                padding2 = padding2 + " "

        enums = ""
        if print_enums:
            enums = get_enum_str(tag_number)

        line = tag_number + padding1 + " | " + tag_name + padding2 + " | " + tag_value + enums + "\n"
        output_file.write(line)
        if use_row_separators:
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
    build_row_separators()
    init_fields()
    parse_input_file()


if __name__ == "__main__":
    main()