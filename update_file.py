def update_file(input_file, output_file):
    
    # Open the target file
    with open(input_file) as f:

        for line in f:
            prefix = "<pre class='cm'>"
            if prefix in line and 'print' in line:
                if line.index(prefix) < line.index('print'):
                    x = line[line.index(prefix):line.index('</pre>')]
                    # x = x[x.find("<")]
                    print(x)
                    
            
update_file("docs.html", "out_file.txt")

