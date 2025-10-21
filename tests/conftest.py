# conftest.py is the equivalent of hooks in C#
import pytest
import subprocess
import sys
import os

def pytest_sessionfinish(session, exitstatus):
    """
    Hook that runs after the entire test session finishes.
    """
    # Path to your report generator script
    report_script = os.path.join("support", "reporting", "generate_docx_report.py")

    if os.path.exists(report_script):
        print("\nGenerating Word report after tests.")
        try:
            # Use the same Python interpreter that ran pytest
            subprocess.run([sys.executable, report_script], check=True)
            print("Word report generation complete.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to generate Word report: {e}")
    else:
        print(f"Could not find report generator script at {report_script}")
