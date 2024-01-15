import os
import argparse
import glob
import shutil
import random

parser = argparse.ArgumentParser(
    prog='cttv',
    description='Create a train, test and validation sets',
    epilog='')
parser.add_argument('--location', help='list of directories to find images and label files', action='store',
                    default='./')
parser.add_argument('--train_per', help='precentage of files to use as a train set', default=45, action='store',
                    type=int)
parser.add_argument('--test_per', help='percentage of files to use for train set', default=45, action='store', type=int)
parser.add_argument('--validate_per', help='precentage of files to use for validation set', default=10, action='store',
                    type=int)
parser.add_argument('--label_extension', choices=['xml', 'json'], default='xml', action='store',
                    help='file extension for lables')


def main(args):
    # configurable options
    img_root = args.location if args.location else './'

    extract_data_from = {
        'LIVELONG': os.path.join(img_root, 'collectedimages', 'livelong'),
        'THANKYOU': os.path.join(img_root, 'collectedimages', 'thankyou'),
        'THUMBSDOWN': os.path.join(img_root, 'collectedimages', 'thumbsdown'),
        'THUMBSUP': os.path.join(img_root, 'collectedimages', 'thumbsup'),
    }

    # these directories should be removed if existed or created or add a flag to say they should only be added to
    # import shutil
    # shutil.rmtree('/path/to/folder')
    place_data_in = {
        'TRAIN': os.path.join(img_root, 'train/'),
        'TEST': os.path.join(img_root, 'test/'),
        'VALIDATE': os.path.join(img_root, 'validation/'),
    }

    # end configurable options

    # clean out and create train/test/validate directories
    for key, data_dir in place_data_in.items():
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        os.mkdir(data_dir)


    for key, path in extract_data_from.items():
        files = sorted(glob.glob(os.path.join(path, '*.' + args.label_extension)))
        number_of_files = len(files)
        number_of_training_files = int( number_of_files * args.train_per/100 )
        number_of_testing_files = int( number_of_files * args.train_per/100 )
        number_of_validation_files = int( number_of_files * args.validate_per/100 )
        if number_of_files != sum([number_of_training_files, number_of_testing_files, number_of_validation_files ]):
            print("warning files can not be split according to percentages given.")

        #train

        for x in range(number_of_training_files):
            # get file list. this will be used so we don't add the same file to two different directories
            random_element = random.choice(files)
            file_name = os.path.splitext(random_element)
            for list_item in glob.glob(file_name[0]+'.*'):
                shutil.copy(list_item, place_data_in['TRAIN'])

        #test

        for x in range(number_of_testing_files):
            random_element = random.choice(files)
            file_name = os.path.splitext(random_element)
            for list_item in glob.glob(file_name[0] + '.*'):
                shutil.copy(list_item, place_data_in['TEST'])

        #validate
        for x in range(number_of_validation_files):
            random_element = random.choice(files)
            file_name = os.path.splitext(random_element)
            for list_item in glob.glob(file_name[0] + '.*'):
                shutil.copy(list_item, place_data_in['VALIDATION'])


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
