from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
from PIL import Image
import os
import tensorflow as tf
import base64

app = Flask(__name__)

# Function to process the uploaded image
def process_image(file, save_path):
    # Read the image using PIL
    img = Image.open(file)
    # Convert the image to a NumPy array
    img_array = np.array(img)
    # Write the image array to a file using OpenCV
    cv2.imwrite(save_path, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

def predict_category(img_path, model_path, target_size=(224, 224)):
    # Read the image
    img = cv2.imread(img_path)
    
    # Check if the image is loaded successfully
    if img is None:
        raise ValueError("Error loading image. Please check the image path.")
    
    # Check if the image has a valid size
    if img.size == 0:
        raise ValueError("Empty image. Please provide a valid image.")

    # Resize the image
    img = cv2.resize(img, target_size)
    
    # Apply CLAHE to each channel separately
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = cv2.merge([clahe.apply(channel) for channel in cv2.split(img)])
    clahe_image = np.expand_dims(clahe_image, axis=0)  # Expand dimensions

    # Load the pre-trained model
    model = tf.keras.models.load_model(model_path)

    # Predict category
    predictions = model.predict(clahe_image)

    # Get category name and probability
    class_names = ['Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot','Tomato___Spider_mites Two-spotted_spider_mite',
                    'Tomato___Target_Spot','Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus','Tomato___healthy']
    
    category_index = np.argmax(predictions)
    category_name = class_names[category_index]
    probability = predictions[0][category_index]

    # Return category name and probability
    return img,category_name, probability

# Route to display the upload form and handle the file upload
@app.route('/', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        # Check if a file was submitted
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        # Check if a file was selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        # Process the uploaded file
        try:
            process_image(file, 'static/output.JPG')
            img,category_name,prob = predict_category('static/output.JPG', 'model_2.h5', target_size=(224, 224))
            os.remove('static/output.JPG')
            # Convert the image to base64 format
            retval, buffer = cv2.imencode('.jpg', img)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            # Pass the base64 encoded image to the HTML template
            return render_template(f'{category_name}.html',image = image_base64)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
