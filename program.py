import os
from PIL import Image


def main():
    sizes = [64, 128, 512]

    # get input from args
    if len(os.sys.argv) < 2:
        print("Usage: program.py <input_file>")
        exit(1)

    folder_path = os.sys.argv[1]

    for size in sizes:
        dir_name = '%s/%dx%d' % (folder_path, size, size)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    # for loop for all images in directory
    for file in os.listdir(folder_path):
        # if is png file
        if not file.endswith('.png'):
            continue

        image = Image.open(folder_path + '/' + file)
        # get file name from full path
        filename = os.path.basename(file)

        (width, height) = image.size
        main = width if width > height else height

        for size in sizes:
            ratio = size / main
            newImage = image.resize((int(width * ratio), int(height * ratio)))
            newImage.save('%s/%dx%d/%s' % (folder_path, size, size, filename))


if __name__ == '__main__':
    main()
