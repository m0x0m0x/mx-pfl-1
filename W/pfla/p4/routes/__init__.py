from routes import main
from flask import Blueprint

# Create main blueprint
bp = Blueprint('main', __name__)

# Import routes (must be at bottom to avoid circular imports)
