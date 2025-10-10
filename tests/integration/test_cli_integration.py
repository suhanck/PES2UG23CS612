"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        cmd = [sys.executable, "-m", "src.cli"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "4", "7")
        assert result.returncode == 0
        assert result.stdout.strip() == "28"

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "15", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"

    def test_cli_power_integration(self):
        """Test CLI can perform power operation"""
        result = self.run_cli("power", "2", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_square_root_integration(self):
        """Test CLI can perform square root"""
        result = self.run_cli("sqrt", "16")
        assert result.returncode == 0
        assert result.stdout.strip() == "4"

    def test_cli_square_root_alias_integration(self):
        """Test CLI can perform square root with alias"""
        result = self.run_cli("square_root", "25")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"
