import filemagic


def detect_archive_format(file_path):
    mime = filemagic.Magic()
    file_type = mime.from_file(file_path)

    if 'archive' in file_type:
        return True
    else:
        return False


file_path = 'path_to_your_file'
is_archive = detect_archive_format(file_path)

if is_archive:
    print(f"The file '{file_path}' is likely an archive.")
else:
    print(f"The file '{file_path}' is not recognized as an archive.")
