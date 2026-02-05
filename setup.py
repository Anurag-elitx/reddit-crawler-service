from setuptools import setup, find_packages

setup(
    name="social-insight-engine",
    version="0.1.0",
    description="An AI-assisted pipeline for discovering, extracting, and structuring social media conversations.",
    author="Open Source Contributor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "django>=4.0",
        "psycopg2-binary",
        "langchain",
        "notebook",
    ],
    python_requires=">=3.8",
)
