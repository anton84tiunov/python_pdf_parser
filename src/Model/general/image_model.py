class BaseImageModel():

    def __init__(self):
        self.ext: str = ...
        self.smask: int = ...
        self.width: int = ...
        self.height: int = ...
        self.colorspace: int = ...
        self.bpc: int = ...
        self.xres: int = ...
        self.yres: int = ...
        self.cs_name: str = ...
        self.image: bytes = ...


class ImageModel():

    def __init__(self):
        self.img: tuple[int, int, int, int, int, str, str, str, str] = ...
        self.base_image: BaseImageModel = ...
        self.bbox: tuple[float, float, float, float] = ...
        self.img: tuple[float, float, float, float, float, float] = ...








         # image[""]
            # print(img)
            # (10, 0, 4000, 4000, 8, 'DeviceRGB', '', 'FXX1', 'DCTDecode')  
            # print(base_image.keys())
            # dict_keys(['ext', 'smask', 'width', 'height', 'colorspace', 'bpc', 'xres', 'yres', 'cs-name', 'image'])
            # print(bbox)
            # Rect(363.0459899902344, 586.7990112304688, 561.468017578125, 774.1580200195312)
            # print(transform)
            # Matrix(198.4219970703125, 0.0, -0.0, 187.35899353027344, 363.0459899902344, 586.7990112304688)
           





