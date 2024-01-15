import os
import argparse
import glob

parser = argparse.ArgumentParser(
                    prog='cttv',
                    description='Create a train, test and validation sets',
                    epilog='')
parser.add_argument('--location', help='list of directories to find images and label files', action='store', default='./' )
parser.add_argument('--train_per', help='precentage of files to use as a train set', default=45, action='store', type=int)   
parser.add_argument('--test_per', help='percentage of files to use for train set', default=45, action='store', type=int)    
parser.add_argument('--validate_per', help='precentage of files to use for validation set', default=10, action='store', type=int)  
parser.add_argument('--lable_extension', choices['xml', 'json'], default='xml', action='store', help='file extension for lables' )  


def main(args):
    # configurable options
    img_root = os.path(args.location) 

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

    # end configurable options

    # get file list. this will be used so we don't add the same file to two different directories
    dir_list = {}
    for key, path in extract_data_from:
        files = glob.glob(os.path.join(path,'*.'+args.lable_extension))
        print(files)

    

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
