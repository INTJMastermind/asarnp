import os
from _paths import *

file_names = os.listdir(NAVDATA_FOLDER)
source_names = [SOURCE_FOLDER+file_name for file_name in file_names]
data_names = [NAVDATA_FOLDER+file_name for file_name in file_names]
output_names = source_names
#output_names = [OUTPUT_FOLDER+file_name for file_name in file_names]


def read_datafile(file_name):
    with open(file_name) as file:
        return file.read().splitlines()
    

def process_navdata(data):
    fixes = [line for line in data if line.startswith("FIX")]
    sids = [line for line in data if line.startswith("SID") or line.startswith(" RNW") or line.startswith("  TRANSITION")]
    approaches = [line for line in data if line.startswith("APPROACH") or line.startswith(" TRANSITION")]
    return fixes, sids, approaches


def insert_data(source, data, marker):
    if marker in source:
        idx = source.index(marker)
        # Don't insert data that's already in the source file
        new_data = [line for line in data if line not in source]
        source[idx:idx] = new_data
        print(f"{len(new_data)} lines inserted.")
    else:
        print(f"Error: {marker} not found! No lines inserted.")


def write_navdata(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            f.write(line + '\n')


def update_navdata(file_name, data_name, source_name, output_name):
    print(f'Reading {data_name}.')
    fixes, sids, approaches = process_navdata(read_datafile(data_name))
    print(f'{len(fixes)} Fixes, {len(sids)} SIDS, {len(approaches)} Approaches Found.')

    print(f'Opening {source_name}...')
    source = read_datafile(source_name)
    print(f'{len(source)} lines opened')

    print(f"Inserting Fixes into {file_name}.")
    insert_data(source, fixes, "ENDFIXES")

    print(f"Inserting SIDS into {file_name}.")
    insert_data(source, sids, "ENDSIDS")

    print(f"Inserting Approaches into {file_name}.")
    insert_data(source, approaches, "ENDAPPROACHES")

    print(f"Writing output file: {output_name}")
    write_navdata(output_name, source)
    print(f"{len(source)} lines successfully written!\n")


def main():
    for file_name, data_name, source_name, output_name in zip(file_names, data_names, source_names, output_names):
        update_navdata(file_name, data_name, source_name, output_name)


if __name__ == "__main__":
    main()