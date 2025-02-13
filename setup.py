import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text-Concise-AI"
AUTHOR_USER_NAME = "harditrivedi16"
SRC_REPO = "textConciseAI"
AUTHOR_EMAIL = "harditrivedi16@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = ("Python based text summary generator"),
    url = f"https://github.com/harditrivedi16/Text-Concise-AI",
    project_urls= {
        "Bug Tracker": f"https://github.com/harditrivedi16/{REPO_NAME}/issues",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
    
)
