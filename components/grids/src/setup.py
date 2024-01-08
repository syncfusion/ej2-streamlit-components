import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ej2_streamlit_grids",
    version="24.1.41",
    author="Syncfusion",
    author_email="info@syncfusion.com",
    description="Streamlit component implementation of Syncfusion Grid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syncfusion/ej2-streamlit-components/tree/master/components/grids/src",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.75",
    ],
)
