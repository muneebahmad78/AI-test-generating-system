#!/usr/bin/env python3
"""
AI-Powered Automated Test Generator
====================================

Main entry point for the test generator.

Usage:
    python main.py generate <source_file.py>
    python main.py analyze <source_file.py>
    python main.py coverage <test_file.py> <source_file.py>
    python main.py run <test_file.py>

For more options:
    python main.py --help
    python main.py generate --help
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.cli import main

if __name__ == "__main__":
    main()

