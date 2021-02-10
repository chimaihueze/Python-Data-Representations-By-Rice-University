def update_file(input_file, output_file):
    with open(input_file) as f:
        for line in f:
            print(line)
            
update_file("docs.html", "out_file.txt")