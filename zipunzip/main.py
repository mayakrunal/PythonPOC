import zipfile

if __name__ == '__main__':
    with open('file1.txt', 'w+') as f:
        f.write('One File')

    with open('file2.txt', 'w+') as f:
        f.write('Two File')

    with zipfile.ZipFile('comp_file.zip', 'w') as comp_file:
        comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
        comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile('comp_file.zip', 'r') as zip_obj:
        zip_obj.extractall('extracted')
