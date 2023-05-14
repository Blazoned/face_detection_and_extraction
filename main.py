import cv2
import os
import sys

PATH_HAAR_CASCADES = os.path.join(os.getcwd(), '.resources', 'frontalface_default_haarcascade.xml')
FACE_CASCADE = cv2.CascadeClassifier(PATH_HAAR_CASCADES)

def find_faces(image_path):
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image, FACE_CASCADE.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

def save_faces(output_folder, faces_coordinates, image, face_index_memo):
    face_index = face_index_memo[0]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, (x, y, w, h) in enumerate(faces_coordinates):
        face = image[y:y + h, x:x + w]
        face = cv2.resize(face, (48, 48))
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save the face image
        face_filename = f"face_{face_index + i}.jpg"
        face_path = os.path.join(output_folder, face_filename)
        cv2.imwrite(face_path, face_gray)

        print(f"Face {face_index + i + 1} saved as {face_filename}")

    face_index_memo[0] = face_index + len(faces_coordinates)

def detect_faces(image_path, output_folder, face_index_memo:list=[0]):
    image, faces_coordinates = find_faces(image_path)
    save_faces(output_folder, faces_coordinates, image, face_index_memo)


def iterate_folder_image(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            detect_faces(image_path, output_folder)


def load_arguments():
    if sys.argv == 1:
        exit_with_error(41)

    mapping = []

    for folder_mapping in sys.argv[1:]:
        folder_mapping = tuple(folder_mapping.split(':'))

        if len(folder_mapping) != 2:
            exit_with_error(42)

        mapping.append(folder_mapping)

    return mapping


def exit_with_error(code: int = 0):
    print('Usage: python main.py "{input_folder_1}:{output_folder_1}" ["{input_folder_2}:{output_folder_2}" ...]')
    exit(code)


def main():
    mapping = load_arguments()

    for io_map in mapping:
        iterate_folder_image(io_map[0], io_map[1])


if __name__ == '__main__':
    main()
