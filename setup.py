import setuptools

setuptools.setup(
    name="midjourney_api",  # How you named your package folder (MyLib)
    packages=["midjourney_api"],  # Chose the same as "name"
    version="1.0.7",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    long_description=open("README.rst").read(),
    description="Midjourney API wrapper by The Next Leg",  # Give a short description about your library
    author="The Next leg",  # Type in your name
    author_email="support@thenextleg.io",  # Type in your E-Mail
    url="https://github.com/midjourney-api-the-next-leg/python-midjourney-api",  # Provide either the link to your github or to your website
    download_url="https://github.com/midjourney-api-the-next-leg/python-midjourney-api/archive/refs/tags/v1.0.0.tar.gz",  # I explain this later on
    keywords=[
        "MIDJOURNEY",
        "API",
        "THE_NEXT_LEG",
    ],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
