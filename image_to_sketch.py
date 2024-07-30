import cv2

def load_and_resize_image(filepath, size=(500, 800)):
    img = cv2.imread(filepath)
    return cv2.resize(img, size)

def add_text(image, text, position, font_scale=1, color=(0,0,0), thickness=1):
    font = cv2.FONT_HERSHEY_DUPLEX 
    return cv2.putText(image, text, position, font, font_scale, color, thickness)

def display_image(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    filepath = "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Screenshots\\lena-1.jpg"
    
    # Original Image
    img = load_and_resize_image(filepath)
    img_with_text = add_text(img.copy(), 'ORIGINAL_IMAGE', (10, 30), color=(0,0,0), thickness=2)
    
    # Grayscale Image
    grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscale_with_text = add_text(grayscale_image.copy(), 'GRAYSCALE', (10, 45), color=(0,0,0), thickness=2)
    
    # Median Blur
    #median_blur = cv2.blur(img, (5, 5))
    median_blur = cv2.medianBlur(grayscale_image, 5)
    median_blur_with_text = add_text(median_blur.copy(), 'MEDIAN_BLUR', (10, 45), color=(0, 0, 0), thickness=2)
    
    # Inverted Image
    inverted_image = cv2.bitwise_not(median_blur)
    inverted_image_with_text = add_text(inverted_image.copy(), 'INVERTED_IMAGE', (10, 45), color=(0, 0, 0), thickness=2)
    
    # Sketch
    blur = cv2.GaussianBlur(inverted_image, (211, 211), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grayscale_image, inverted_blur, scale=256.0)
    sketch_with_text = add_text(sketch.copy(), 'SKETCH', (10, 45), color=(0,0,0), thickness=2)
    
    # Display Images
    display_image("Original Image", img_with_text)
    display_image("Grayscale Image", grayscale_with_text)
    display_image("Median Blur", median_blur_with_text)
    display_image("Inverted Image", inverted_image_with_text)
    display_image("Sketch", sketch_with_text)
if __name__ == "__main__":
    main()
