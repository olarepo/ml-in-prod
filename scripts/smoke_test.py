import sys
import platform
import importlib

def check_import(pkg_name: str):
    try:
        importlib.import_module(pkg_name)
        print(f"✔ {pkg_name} imported successfully")
    except ImportError:
        print(f"✖ Failed to import {pkg_name}")
        sys.exit(1)

def main():
    print("Running smoke test...\n")

    print(f"Python version: {platform.python_version()}")

    packages = [
        "pandas",
        "numpy",
        "sklearn",
        "pydantic",
        "yaml",
        "joblib",
        "fastapi",
    ]

    for pkg in packages:
        check_import(pkg)

    print("\n✅ Smoke test passed.")

if __name__ == "__main__":
    main()
