
def get_mime_type(filename):
    # Remove spaces and convert to lowercase
    filename = filename.strip().lower()

    # If no dot in filename, return default
    if "." not in filename:
        return "application/octet-stream"

    # Take the part after the last dot
    ext = filename.split(".")[-1]

    # Dictionary mapping extensions to MIME types
    mime_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    # Use .get() to return the value if it exists,
    # otherwise return the default
    return mime_types.get(ext, "application/octet-stream")


def main():
    name = input("File name: ")
    print(get_mime_type(name))


main()


