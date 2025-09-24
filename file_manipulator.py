from pathlib import path

def reverse_lines_streaming(input_path: str,output_path: str, *,encoding: str = "utf-8"):
    in_p = path(input_path)
    out_p = path(output_path)








def reverse(input_path,output_path):
    contents = ''
    
    with open(input_path) as f:
        contents = f.read()
    
    with open(output_path,'w') as f:
        f.write(helperReverse(contents))

def helperReverse(words):
    contents = ""
    for i in range(len(words)):
        for j in range(-1,0):
            contents += 
