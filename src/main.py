from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


DEFAULT_TEST_SIZE = 0.3
DEFAULT_AUGMENT_SIZE = 0.6


def setup_parser(parser):
    parser.add_argument(
        '-n', "--num_train", required=True,
        help='the total number of images in the training dataset including real, augmented and generated data.',
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
    print(arguments)


if __name__ == "__main__":
    main()
