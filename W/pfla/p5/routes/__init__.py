# Just collect and export all blueprints
from .debug import debug_bp
from .main import main_bp
from .tezt import tezt_bp

__all__ = ['main_bp', 'tezt_bp', 'debug_bp']
