import cv2


class Parser:
    @staticmethod
    def parse_annotations(annotations):
        pass

    @staticmethod
    def get_annotations(image_path):
        return None, None


class CocoParser(Parser):
    @staticmethod
    def parse_annotations(annotations):
        pass


class ImageProcessor:
    def __init__(self, image_path, annotations):
        self.image = cv2.imread(image_path)
        self.annotations = Parser.get_annotations(annotations)

    def preprocessing(self):
        self._resize()
        self._rotate()
        self._padding()

    def _resize(self):
        pass

    def _padding(self):
        pass

    def _rotate(self):
        pass
