"""
AI Test Generator - Configuration
==================================

Central configuration for the test generator.
"""

from dataclasses import dataclass, field
from typing import Optional, List
from pathlib import Path
import os


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""
    provider: str = "auto"  # auto, openai, anthropic, local
    model: Optional[str] = None
    api_key: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 4096
    
    def __post_init__(self):
        # Load API keys from environment if not provided
        if self.api_key is None:
            if self.provider == "openai":
                self.api_key = os.getenv("OPENAI_API_KEY")
            elif self.provider == "anthropic":
                self.api_key = os.getenv("ANTHROPIC_API_KEY")


@dataclass
class TestGenerationConfig:
    """Configuration for test generation."""
    target_coverage: float = 90.0
    max_regeneration_iterations: int = 3
    include_edge_cases: bool = True
    include_parametrized_tests: bool = True
    include_docstrings: bool = True
    test_file_prefix: str = "test_"
    
    # Edge case configuration
    test_null_values: bool = True
    test_empty_values: bool = True
    test_boundary_values: bool = True
    test_type_errors: bool = True
    test_exceptions: bool = True


@dataclass
class CoverageConfig:
    """Configuration for coverage measurement."""
    branch_coverage: bool = True
    show_missing_lines: bool = True
    html_report: bool = False
    html_output_dir: str = "htmlcov"
    fail_under: float = 0.0  # 0 means don't fail


@dataclass
class OutputConfig:
    """Configuration for output and reporting."""
    tests_directory: str = "tests"
    verbose: bool = False
    use_rich: bool = True
    show_generated_code: bool = False
    save_prompts: bool = False  # Save LLM prompts for debugging


@dataclass
class Config:
    """Main configuration class."""
    llm: LLMConfig = field(default_factory=LLMConfig)
    test_generation: TestGenerationConfig = field(default_factory=TestGenerationConfig)
    coverage: CoverageConfig = field(default_factory=CoverageConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    
    # Paths
    working_directory: Optional[str] = None
    
    @classmethod
    def from_file(cls, config_path: str) -> 'Config':
        """Load configuration from a JSON or YAML file."""
        import json
        
        path = Path(config_path)
        if not path.exists():
            return cls()
        
        with open(path, 'r') as f:
            data = json.load(f)
        
        return cls(
            llm=LLMConfig(**data.get('llm', {})),
            test_generation=TestGenerationConfig(**data.get('test_generation', {})),
            coverage=CoverageConfig(**data.get('coverage', {})),
            output=OutputConfig(**data.get('output', {})),
            working_directory=data.get('working_directory')
        )
    
    def to_dict(self) -> dict:
        """Convert configuration to dictionary."""
        from dataclasses import asdict
        return asdict(self)


# Default configuration instance
default_config = Config()

