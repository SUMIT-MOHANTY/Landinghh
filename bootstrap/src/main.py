import os
import sys

# Add bootstrap directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Create app using factory pattern
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    # Run the application
    app.run(host='0.0.0.0', port=port, debug=debug)
