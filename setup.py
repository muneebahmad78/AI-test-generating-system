"""
AI Test Generator - Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="ai-test-generator",
    version="1.0.0",
    author="AI Test Generator",
    description="AI-powered automated test generation for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/ai-test-generator",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "typer>=0.9.0",
        "astunparse>=1.6.3",
        "openai>=1.0.0",
        "anthropic>=0.18.0",
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "pytest-timeout>=2.2.0",
        "coverage>=7.3.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "jinja2>=3.1.0",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "mypy",
            "flake8",
        ]
    },
    entry_points={
        "console_scripts": [
            "ai-test-gen=src.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
    ],
    keywords="testing, pytest, ai, llm, code-coverage, test-generation",
)

