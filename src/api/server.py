"""
API Server for Daistudio - Image Generation Suite
"""
from flask import Flask, jsonify, request
import os

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Configuration
    app.config['JSON_SORT_KEYS'] = False
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({
            'status': 'healthy',
            'service': 'Daistudio API',
            'version': '1.0.0'
        }), 200
    
    # Image generation endpoint (placeholder)
    @app.route('/api/generate', methods=['POST'])
    def generate_image():
        try:
            data = request.get_json()
            prompt = data.get('prompt', '')
            
            if not prompt:
                return jsonify({'error': 'Prompt is required'}), 400
            
            # TODO: Implement actual image generation logic
            return jsonify({
                'status': 'success',
                'message': 'Image generation in progress',
                'prompt': prompt
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)