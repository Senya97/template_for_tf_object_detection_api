from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib import Path
from utils.dataset_creator_class import DatasetCreator

DEFAULT_NUM_TRAIN = 10
DEFAULT_TEST_SIZE = 0.3
DEFAULT_AUGMENT_SIZE = 0.6
DEAFULT_IMAGES_PATH = Path('../../data/raw/images/')
DEFAULT_GRUND_TRURH_PATH = Path('../../data/raw/annotations')


def setup_parser(parser):
    parser.add_argument(
        '-i', "--images_path", default=DEAFULT_IMAGES_PATH,
        help='path to the folder with images from the dataset'
    )
    parser.add_argument(
        '-g', "--ground_truth_path", default=DEFAULT_GRUND_TRURH_PATH,
        help='path to folder with grund truth'
    )
    parser.add_argument(
        '-n', "--num_train", default=DEFAULT_NUM_TRAIN,
        help='the total number of images in the training dataset including real, augmented and generated data',
    )
    parser.add_argument(
        '-t', "--test_size", default=DEFAULT_TEST_SIZE,
        help='the proportion of real images in the test dataset relative to the number of source images',
    )
    parser.add_argument(
        '-a', "--aug_size", default=DEFAULT_AUGMENT_SIZE,
        help='the proportion of augmented images in the train dataset relative to the generated images',
    )


def main():
    """It is Python CLI application for Dataset Creator. """

    parser = ArgumentParser(
        description='Dataset Creator Application',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    dataset_creator = DatasetCreator(arguments.images_path, arguments.ground_truth_path,
                                     arguments.num_train, arguments.test_size, arguments.aug_size)
    print('add original images ...')
    dataset_creator.add_original_images()
    print('add augmented images ...')
    dataset_creator.add_augmented_images()
    print('add generated images ...')
    dataset_creator.add_generated_images()


if __name__ == "__main__":
    main()
