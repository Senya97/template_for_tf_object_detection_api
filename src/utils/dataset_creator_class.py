from .data_loader_class import XmlDataLoader


class DatasetCreator:
    def __init__(self, images_path, ground_truth_path, num_train=10, test_size=0.3, aug_size=0.6, data_loader=None):
        data_loader = data_loader or XmlDataLoader()
        self.images = data_loader.load_images(images_path)
        self.ground_truth = data_loader.load_ground_truth(ground_truth_path)
        self.num_train = num_train
        self.test_size = test_size
        self.aug_size = aug_size

    def add_original_images(self):
        pass

    def add_augmented_images(self):
        pass

    def add_generated_images(self):
        pass
