# AI-Powered Automated Test Generator

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent test generation system that uses **static code analysis** and **LLM-based reasoning** to automatically generate comprehensive PyTest unit tests for Python code.

## 🎯 Features

- **Static Code Analysis**: Uses Python's AST to analyze code structure, detect functions, classes, branches, and logic patterns
- **AI-Powered Test Generation**: Leverages LLMs (OpenAI GPT-4, Anthropic Claude) to generate high-quality test cases
- **Automatic Edge Case Detection**: Identifies and includes tests for null values, empty inputs, boundary conditions, and exceptions
- **Coverage-Driven**: Measures code coverage and can regenerate tests to achieve ≥90% coverage
- **Clean Code Output**: Generates well-formatted, documented PyTest test files
- **Beautiful Reports**: Rich terminal output with detailed coverage reports

## 📋 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      INPUT LAYER                             │
│                  (Python Source File)                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   ANALYSIS LAYER                             │
│  ┌─────────────────┐     ┌─────────────────┐                │
│  │   AST Analyzer  │     │   Code Parser   │                │
│  │  - Functions    │     │  - Testable     │                │
│  │  - Classes      │     │    Units        │                │
│  │  - Branches     │     │  - Dependencies │                │
│  │  - Complexity   │     │  - Signatures   │                │
│  └─────────────────┘     └─────────────────┘                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                      AI LAYER                                │
│  ┌─────────────────┐     ┌─────────────────┐                │
│  │   LLM Client    │     │  Edge Case      │                │
│  │  - OpenAI       │     │  Detector       │                │
│  │  - Anthropic    │     │  - Null/Empty   │                │
│  │  - Local        │     │  - Boundaries   │                │
│  └─────────────────┘     │  - Exceptions   │                │
│                          └─────────────────┘                │
│  ┌─────────────────────────────────────────┐                │
│  │         Test Generator                   │                │
│  │  - Prompt Engineering                    │                │
│  │  - Test Case Generation                  │                │
│  │  - Code Formatting                       │                │
│  └─────────────────────────────────────────┘                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   TESTING LAYER                              │
│  ┌─────────────────┐     ┌─────────────────┐                │
│  │   Test Runner   │     │    Coverage     │                │
│  │  - PyTest       │     │    Analyzer     │                │
│  │  - Results      │     │  - Coverage.py  │                │
│  │  - Validation   │     │  - Reports      │                │
│  └─────────────────┘     └─────────────────┘                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  REPORTING LAYER                             │
│  ┌─────────────────────────────────────────┐                │
│  │        Coverage Reporter                 │                │
│  │  - Terminal Output (Rich)                │                │
│  │  - Summary Statistics                    │                │
│  │  - Uncovered Lines                       │                │
│  │  - HTML Reports                          │                │
│  └─────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Installation

1. **Clone or download the project**:
   ```bash
   cd ai-test-generator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys** (optional, for LLM-powered generation):
   ```bash
   # For OpenAI
   set OPENAI_API_KEY=your-api-key-here  # Windows
   export OPENAI_API_KEY=your-api-key-here  # Linux/macOS
   
   # For Anthropic Claude
   set ANTHROPIC_API_KEY=your-api-key-here  # Windows
   export ANTHROPIC_API_KEY=your-api-key-here  # Linux/macOS
   ```

### Basic Usage

**Generate tests for a Python file**:
```bash
python main.py generate examples/calculator.py
```

**Generate tests with specific options**:
```bash
python main.py generate examples/calculator.py \
    --output tests \
    --provider anthropic \
    --target-coverage 95 \
    --verbose
```

**Analyze a file without generating tests**:
```bash
python main.py analyze examples/calculator.py --verbose
```

**Run tests and show coverage**:
```bash
python main.py coverage tests/test_calculator.py examples/calculator.py
```

## 📖 Commands

### `generate`

Generate unit tests for a Python source file.

```bash
python main.py generate <source_file.py> [OPTIONS]
```

**Options**:
| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output directory for tests | `tests` |
| `-p, --provider` | LLM provider (`openai`, `anthropic`, `local`) | Auto-detect |
| `-m, --model` | Specific model to use | Provider default |
| `-k, --api-key` | API key for LLM provider | From environment |
| `-c, --target-coverage` | Target coverage percentage | `90` |
| `-i, --max-iterations` | Max regeneration iterations | `3` |
| `--run-tests/--no-run-tests` | Run tests after generation | `True` |
| `-v, --verbose` | Enable verbose output | `False` |

### `analyze`

Analyze a Python source file and display code structure.

```bash
python main.py analyze <source_file.py> [OPTIONS]
```

**Options**:
| Option | Description |
|--------|-------------|
| `-v, --verbose` | Show detailed analysis |

### `coverage`

Run tests and display coverage report.

```bash
python main.py coverage <test_file.py> <source_file.py> [OPTIONS]
```

**Options**:
| Option | Description |
|--------|-------------|
| `--html` | Generate HTML coverage report |

### `run`

Run tests without generating new ones.

```bash
python main.py run <test_file.py> [OPTIONS]
```

**Options**:
| Option | Description |
|--------|-------------|
| `-v, --verbose` | Verbose test output |

## 🧪 Example

### Input: `calculator.py`

```python
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b
```

### Generated: `test_calculator.py`

```python
import pytest
from calculator import divide, DivisionByZeroError


class TestDivide:
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5.0
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
    
    def test_divide_by_one(self):
        """Test division by one returns the dividend."""
        assert divide(7, 1) == 7.0
    
    def test_divide_zero_dividend(self):
        """Test zero divided by non-zero."""
        assert divide(0, 5) == 0.0
    
    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError):
            divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (100, 4, 25.0),
    ])
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized tests for common division cases."""
        assert divide(a, b) == expected
```

## 🔧 Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key for GPT models |
| `ANTHROPIC_API_KEY` | Anthropic API key for Claude models |

### LLM Providers

1. **OpenAI** (GPT-4, GPT-3.5-turbo)
   - Best for: General test generation
   - Default model: `gpt-4o`

2. **Anthropic Claude** (Claude 3)
   - Best for: Complex reasoning, edge cases
   - Default model: `claude-sonnet-4-20250514`

3. **Local** (Template-based)
   - Best for: Quick testing without API
   - No API key required

## 📊 AI4SE Concepts Demonstrated

This project demonstrates key **AI for Software Engineering (AI4SE)** concepts:

1. **Static Code Analysis**: Using AST to understand code structure without execution
2. **LLM-Based Code Understanding**: Leveraging language models to comprehend code semantics
3. **Automated Test Generation**: AI-driven creation of comprehensive test suites
4. **Coverage-Driven Development**: Using coverage metrics to guide test improvement
5. **Edge Case Detection**: Intelligent identification of boundary conditions and error scenarios
6. **Prompt Engineering**: Crafting effective prompts for code-related tasks

## 📁 Project Structure

```
ai-test-generator/
├── src/
│   ├── __init__.py
│   ├── cli.py                    # Command-line interface
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── ast_analyzer.py       # AST-based code analysis
│   │   └── code_parser.py        # High-level code parsing
│   ├── generator/
│   │   ├── __init__.py
│   │   ├── llm_client.py         # LLM provider abstraction
│   │   ├── test_generator.py     # Test generation logic
│   │   └── edge_cases.py         # Edge case detection
│   ├── executor/
│   │   ├── __init__.py
│   │   ├── test_runner.py        # PyTest execution
│   │   └── coverage_analyzer.py  # Coverage measurement
│   └── reporter/
│       ├── __init__.py
│       └── coverage_report.py    # Coverage reporting
├── examples/
│   ├── calculator.py             # Example source file
│   └── string_utils.py           # Example source file
├── tests/                        # Generated tests directory
├── main.py                       # Entry point
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with [Python AST](https://docs.python.org/3/library/ast.html)
- Testing powered by [PyTest](https://pytest.org/)
- Coverage by [Coverage.py](https://coverage.readthedocs.io/)
- LLM integration via [OpenAI](https://openai.com/) and [Anthropic](https://anthropic.com/)
- Beautiful output with [Rich](https://rich.readthedocs.io/)

