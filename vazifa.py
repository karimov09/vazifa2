from PIL import Image, ImageFilter
import os


class ImageChanger:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)

    def save_image(self, image, suffix):
        base, ext = os.path.splitext(self.filename)
        new_filename = f"{base}_{suffix}{ext}"
        image.save(new_filename)
        print(f"{new_filename}")
        return new_filename

    def resize(self, size):
        resized_image = self.image.resize(size)
        return self.save_image(resized_image, f"{size[0]}{size[1]}")

    def crop(self, box):
        cropped_image = self.image.crop(box)
        return self.save_image(cropped_image, f"{box[0]}{box[1]}{box[2]}{box[3]}")

    def blur(self, radius=5):
        blurred_image = self.image.filter(ImageFilter.GaussianBlur(radius))
        return self.save_image(blurred_image)

    def passport_formatter(self):
        passport_size = (3*96, 4*96)  
        resized_image = self.image.resize(passport_size)
        return self.save_image(resized_image, "passport")

    def black(self):
        black_white_image = self.image.convert("L")
        return self.save_image(black_white_image)

    def merge(self, second_image_filename, position):
        second_image = Image.open(second_image_filename)
        merged_image = self.image.copy()
        merged_image.paste(second_image, position)
        return self.save_image(merged_image)

filename = "/mnt/data/rasm.jpg"

changer = ImageChanger(filename)

resized_image_path = changer.resize((800, 600))

cropped_image_path = changer.crop((100, 100, 400, 400))

blurred_image_path = changer.blur(10)

passport_image_path = changer.passport_formatter()

black_white_image_path = changer.black()

second_image_filename = "/mnt/data/vazifa/second_image.jpg"
if os.path.exists(second_image_filename):
    merged_image_path = changer.merge(second_image_filename, (50, 50))
else:
    merged_image_path = None

(resized_image_path, cropped_image_path, blurred_image_path, passport_image_path, black_white_image_path, merged_image_path)
