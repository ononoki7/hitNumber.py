from pathlib import Path

def reverse_lines_streaming(input_path: str,output_path: str, *,encoding: str = "cp932"):
    in_p = Path(input_path)
    out_p = Path(output_path)
    
    if not in_p.is_file():
        raise FileNotFoundError(f"入力ファイルが見つかりません: {in_p}")
    
    if in_p.resolve() == out_p.resolve():
        raise ValueError("input_path と outout_path が同一です （破壊防止のため不可）")

    out_p.parent.mkdir(parents=True,exist_ok=True)
    tmp = out_p.with_suffix(out_p.suffix + ".tmp")
    
    with in_p.open("r",encoding=encoding,newline="") as fin, \
        tmp.open("w",encoding=encoding,newline="") as fout:

        for line in fin:
            if line.endswith("\r\n"):
                body, nl = line[:-2], "\r\n"
            elif line.endswith("\n"):
                body, nl = line[:-1], "\n"
            elif line.endswith("\r"):
                body, nl = line[:-1], "\r"
            else:
                body, nl = line, ""
            reversed_body = body[::-1]
            fout.write(reversed_body + nl)
    tmp.replace(out_p)



def copy_input_output(input_path,output_path):
    
    in_p = Path(input_path)
    out_p = Path(output_path)

    if not in_p.is_file():
        raise FileNotFoundError(f"このファイルは存在しておりません:{in_p}")
    
    if in_p.resolve() == out_p.resolve():
        raise FileExistsError("input_path と output_path が同一です")
    
    out_p.parent.mkdir(parents=True,exist_ok=True)
    tmp = out_p.with_suffix(out_p.suffix + ".tmp")
    
    with in_p.open("rb") as fin, \
        tmp.open("wb") as fout:
        
        while True:
            data = fin.read(1024*1024)
            if len(data) == 0:
                break
            fout.write(data)
    tmp.replace(out_p)

def duplicate_input_input(input_path,n):
    in_p = Path(input_path)

    try:
        count = int(n)
    except ValueError:
        raise ValueError("n は整数で指定してください")
    if count < 1:
        raise ValueError("n は 1 以上にしてください")

    if not in_p.is_file():
        raise FileNotFoundError(f"このファイルは存在しません: {in_p}")
    
    tmp = in_p.with_suffix(in_p.suffix + ".tmp")

    with in_p.open("rb") as fin, \
        tmp.open("wb") as fout:
        
        for _ in range(count):
            fin.seek(0)
            while True:
                data = fin.read(1024*1024)
                if not data:
                    break
                fout.write(data)
    tmp.replace(in_p)        



def replace_string_input_input(input_path: str,needle,newstring,*,encoding="cp932"):
    in_p = Path(input_path)
    if needle == "":
        raise ValueError("空白は使えません")

    if not in_p.is_file():
        raise FileNotFoundError(f"このファイルは存在していません: {in_p}")
    
    tmp = in_p.with_suffix(in_p.suffix + ".tmp")

    with in_p.open("r",encoding=encoding,newline="") as fin, \
        tmp.open("w",encoding=encoding,newline="") as fout:

        for line in fin:
            line = line.replace(needle,newstring)
            fout.write(line)
    tmp.replace(in_p)

replace_string_input_input("data/input2.txt","satoru","getou")