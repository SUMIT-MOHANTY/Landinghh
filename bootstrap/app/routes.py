from flask import Blueprint, jsonify, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Root endpoint returning API greeting"""
    return jsonify({"message": "Flask app running"})

@bp.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@bp.route('/home')
def home():
    """Home page using template"""
    return render_template('index.html')

@bp.errorhandler(404)
def not_found(error):
    """Custom 404 handler returning JSON"""
    return jsonify({"error": "Not found"}), 404

@bp.app_errorhandler(404)
def handle_404(error):
    """Global 404 handler"""
    return jsonify({"error": "Not found"}), 404
