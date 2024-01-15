import os


def main():
    # configurable options
    img_root = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

    extract_data_from = {
        'LIVELONG': os.path.join(img_root, 'collectedimages', 'livelong'),
        'THANKYOU': os.path.join(img_root, 'collectedimages', 'thankyou'),
        'THUMBSDOWN': os.path.join(img_root, 'collectedimages', 'thumbsdown'),
        'THUMBSUP': os.path.join(img_root, 'collectedimages', 'thumbsup'),
    }

    place_data_in = {
        'TRAIN': os.path.join(img_root, 'train'),
        'TEST': os.path.join(img_root, 'test'),
        'VALIDATION': os.path.join(img_root, 'validation'),
    }

    # if using labelImg.py label_format='xml', if using labelMe.py label_format='json'
    label_format = 'xml'

    # end configurable options

    # get file list. this will be used so we don't add the same file to two different directories
    dir_list = {}
    for key, path in extract_data_from:
        dir_list[key] = os.listdir(path)



if __name__ == "__main__":
    main()
