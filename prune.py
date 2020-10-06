# -*- coding: utf-8 -*-

import os

rootdir = '.'

def add_mobile_viewport_support(filepath):
    metastr = '    <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    lines = []
    with open(filepath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        if metastr in lines:
            return
        for i in range(len(lines)):
            if lines[i].strip(" ").startswith("<meta"):
                lines.insert(i, metastr)
                break
    with open(filepath, 'w', encoding='UTF-8') as f:
        f.writelines(lines)

def add_footer(filepath):
    footerstr = """
    <footer>
        <p><a href="/search/search.html" target="_self">search</a> | <a href="https://github.com/idelem/trilium-garden" target="_blank">git repo</a></p>
    </footer>\n"""

    lines = []
    newlines = []
    skipping = False

    with open(filepath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if "<footer>" in lines[i]:
                skipping = True
            if "</footer>" in lines[i]:
                skipping = False
                continue
            if skipping:
                continue
            if lines[i].strip(" ").startswith("</body>"):
                newlines.append(footerstr)
            newlines.append(lines[i])

    with open(filepath, 'w', encoding='UTF-8') as f:
        f.writelines(newlines)

exclude_dirs = [".git", "src", "search", "node_modules"]

def is_excluded(subdir):
    for dirname in exclude_dirs:
        if dirname in subdir:
            return True

def main():
    for subdir, dirs, files in os.walk(rootdir):
        if is_excluded(subdir):
            continue
        for file in files:
            filepath = os.path.join(subdir, file)
            if file.endswith(".html"):
                print(filepath)
                add_mobile_viewport_support(filepath)
                add_footer(filepath)

if __name__ == "__main__":
    main()