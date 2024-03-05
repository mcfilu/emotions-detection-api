# Face Detection Blur API
This API provides functionality to apply a blur effect to faces detected in uploaded images.

# App currently in progress!!!

## Usage
### Endpoints
GET /: Root endpoint providing basic information about the application.

POST /filters/blur: Endpoint to apply a blur effect to an uploaded image.

### Parameters
file: The uploaded image file.
depth: The depth of the blur effect (default: 30, range: 0-100).
### Response
The endpoint returns a streaming response containing the processed image with the blur effect applied.

## Supported Content Types
Only image/jpeg content type is supported.

## Setup
Clone the repository: git clone https://github.com/mcfilu/face-detection-blur-api.git

Install dependencies: pip install -r requirements.txt

Run the application: uvicorn app:app --reload

## Examples
Apply Blur Effect
```bash
curl -X POST \
  -F "file=@/path/to/your/image.jpg" \
  -F "depth=50" \
  http://localhost:8000/filters/blur
```
Replace /path/to/your/image.jpg with the path to your image file.

## Dependencies
FastAPI
OpenCV
mtcnn
TensorFlow (for face detection)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
