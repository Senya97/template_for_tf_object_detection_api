from pathlib import Path

from .utils import ImageProcessor, CocoParser

IMAGES_PATH = Path('../../data/raw/images/')
ANNOTATIONS_PATH = Path('../../data/raw/annotations')


class DatasetCreator:
    def __init__(self, num_train, test_size, aug_size):
        self.num_train = num_train
        self.test_size = test_size
        self.aug_size = aug_size
        self._load_data(IMAGES_PATH, ANNOTATIONS_PATH)

    def _load_data(self, images_path, annotations_path):
        self.images = images_path.glob('*')
        self.annotations = CocoParser.parse_annotations(annotations_path)

    def _save_data(self, image, annotations):
        pass

    def add_original_images(self):
        for image_path in self.images:
            image_processor = ImageProcessor(image_path, self.annotations)
            image_processor.preprocessing()
            image = image_processor.image
            annotations = image_processor.annotations
            self._save_data(image, annotations)

    def add_original_images(self):
        pass

    def add_augmented_images(self):
        pass

    def add_generated_images(self):
        pass
