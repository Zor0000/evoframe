import picamera
from time import sleep

def capture_image(file_path='captured_image.jpg'):
    with picamera.PiCamera() as camera:

        sleep(2)

        camera.capture(file_path)

if __name__ == "__main__":
    image_file_path = 'captured_image.jpg'

    capture_image(image_file_path)

    print(f"Image captured and saved to {image_file_path}")
