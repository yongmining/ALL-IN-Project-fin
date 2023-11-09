import argparse
from flask_cors import CORS  # CORS 추가
import app

if __name__ == "__main__":
    deepface_app = app.create_app()

    # CORS 미들웨어 추가
    CORS(deepface_app, resources={r"/api/v1/emotion/analyze": {"origins": ["http://localhost:3000", "http://localhost:8080"], }})

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=5000, help="Port of serving api")
    args = parser.parse_args()
    deepface_app.run(host="0.0.0.0", port=args.port)