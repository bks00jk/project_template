from app.io.input import read_from_console, read_from_file, read_with_pandas
from app.io.output import write_to_console, write_to_file

def main():
    console_text = read_from_console()
    file_text = read_from_file()
    pandas_text = read_with_pandas()

    write_to_console(console_text)
    write_to_console(file_text)
    write_to_console(pandas_text)

    output_file = "output_results.txt"
    write_to_file(console_text, output_file)
    write_to_file(file_text, output_file)
    write_to_file(pandas_text, output_file)

if __name__ == "__main__":
    main()