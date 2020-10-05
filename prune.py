import os

rootdir = '.'

def add_mobile_viewport_support(filepath):
    metastr = '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    lines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        if metastr in lines:
            return
        for i in range(len(lines)):
            if lines[i].strip(" ").startswith("<meta"):
                lines.insert(i, metastr)
                break
    with open(filepath, 'w') as f:
        f.writelines(lines)


def main():
    for subdir, dirs, files in os.walk(rootdir):
        if ".git" in subdir:
            continue
        for file in files:
            filepath = os.path.join(subdir, file)
            print(filepath)
            if file.endswith(".html"):
                add_mobile_viewport_support(filepath)

if __name__ == "__main__":
    main()