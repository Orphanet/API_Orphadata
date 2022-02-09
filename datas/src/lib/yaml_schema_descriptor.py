import pathlib
import json
import time

from . config_orphadata_elastic import *


def recursive_non_empty(elem):
    missing_val = False
    if isinstance(elem, dict):
        for child in elem:
            if elem[child] is None:
                return True
            missing_val = recursive_non_empty(elem[child])
    elif isinstance(elem, list):
        if len(elem) == 0:
            return True
        for sub_elem in elem:
            missing_val = recursive_non_empty(sub_elem)
    return missing_val


def input_type(data, encoding):
    if isinstance(data, type(pathlib.Path())):
        # print("Path as input")
        # parse the file keep the first element
        with open(data, "r", encoding=encoding) as ini:
            for line in ini:
                missing_val = False
                # skip index declaration
                if not line.startswith("{\"index\": {\"_index\":"):
                    data = json.loads(line)
                    missing_val = recursive_non_empty(data)
                    if missing_val:
                        # Will return the last elem even if missing value
                        pass
                    else:
                        break
    return data


def recursive_format_schema(data, main_indent):
    prop_list = list()
    for key, value in data.items():
        # print(key)
        if isinstance(value, str):
            prop = '{}{}:\n'.format(main_indent, key) + \
                   '{}  type: string\n'.format(main_indent) + \
                   '{}  example: \"{}\"\n'.format(main_indent, value)
            prop_list.append(prop)

        elif isinstance(value, dict):
            prop = '{}{}:\n'.format(main_indent, key) + \
                   '{}  type: object\n'.format(main_indent) + \
                   '{}  properties:\n'.format(main_indent)

            prop_list.append(prop)

            indent = main_indent + "    "
            prop = recursive_format_schema(value, indent)
            prop_list.append("".join(prop))

        elif isinstance(value, list):
            if len(value) > 0:
                prop = '{}{}:\n'.format(main_indent, key) + \
                       '{}  type: array\n'.format(main_indent) + \
                       '{}  items:\n'.format(main_indent)
                prop_list.append(prop)
                if isinstance(value[0], dict):
                    indent = main_indent + "  "
                    prop = '{}  type: object\n'.format(indent) + \
                           '{}  properties:\n'.format(indent)
                    prop_list.append(prop)

                    indent = main_indent + "      "

                    prop = recursive_format_schema(value[0], indent)
                    prop_list.append("".join(prop))
                else:
                    prop = '{}    type: string\n'.format(main_indent) + \
                           '{}    example: \"{}\"\n'.format(main_indent, value)
                    prop_list.append(prop)
        else:
            # For the remaining None value
            prop = '{}{}:\n'.format(main_indent, key) + \
                   '{}  type: string\n'.format(main_indent) + \
                   '{}  example: \"{}\"\n'.format(main_indent, value)
            prop_list.append(prop)

    prop_list = "".join(prop_list)

    return prop_list


def format_schema(data, name):
    main_indent = " " * 4

    text = ""

    if "product3" in name:
        text = "{}product3_classification_list:\n".format(main_indent) + \
               "{}  type: array\n".format(main_indent) + \
               "{}  items:\n".format(main_indent) + \
               "{}    $ref: \"#/components/schemas/product3\"\n".format(main_indent)

    text += '{}{}:\n'.format(main_indent, name) + \
            '{}  type: object\n'.format(main_indent) + \
            '{}  properties:\n'.format(main_indent)

    indent = main_indent * 2

    var_text = recursive_format_schema(data, indent)
    required = '{}  required:\n'.format(main_indent) + \
               '{}  - ORPHAcode'.format(main_indent)

    schema = text + var_text + required
    return schema


def output_schema(out_file_path, schema):
    with open(out_file_path, "w", encoding="UTF-8") as out:
        out.write(schema)


def yaml_schema(out_folder, in_file_path, output_encoding):
    start = time.time()
    if in_file_path.suffix != ".json":
        print()
        print("File type is not JSON:")
        print("\t", in_file_path)
        print()
        return

    data = input_type(in_file_path, output_encoding)
    # print(data)

    name = in_file_path.stem
    if name.startswith("en_"):
        name = name[3:]
        if "product3" in name:
            name = "product3"

    schema = format_schema(data, name)

    schema_dir = pathlib.Path(out_folder / "schema")
    if not schema_dir.exists():
        schema_dir.mkdir()
    out_file_path = pathlib.Path(str(out_folder) + "\\schema\\" +
                                 str(name) + ".yaml")

    ref_text = "  {}:\n".format(name)
    ref_text += "    $ref: \"schema/{}.yaml#/{}\"".format(name, name)

    output_schema(out_file_path, schema)
    print("yaml_schema", time.time() - start, "s")

    return ref_text


if __name__ == "__main__":
    start = time.time()

    folders = list()
    parse_folder = True

    # single JSON
    # in_file_path = pathlib.Path("data_out\\product3\\en_product3_146.json")

    # List of folder of JSON
    # folders.append(pathlib.Path("data_out\\product1"))
    # folders.append(pathlib.Path("data_out\\product3"))
    folders.append(pathlib.Path("data_out\\product4"))
    # folders.append(pathlib.Path("data_out\\product6"))
    # folders.append(pathlib.Path("data_out\\product9"))

    folders.append(pathlib.Path("data_out\\"))

    # Out folder
    out_folder = pathlib.Path("data_out")

    text = []

    if parse_folder:
        # Process files in designated folders
        for folder in folders:
            for file in folder.iterdir():
                # print(file)
                if file.stem.startswith("en") or file.stem.startswith("new"):
                    print(file)
                    text.append(yaml_schema(out_folder, file, output_encoding))

    else:
        # Process single file
        file = in_file_path
        text.append(yaml_schema(out_folder, file, output_encoding))

    # [print(elem) for elem in text if elem is not None]

    print()
    print(time.time() - start, "s total")
