import setuptools

setuptools.setup(
    name="ej2_streamlit_grids",
    version="1.0.0",
    author="Syncfusion",
    author_email="info@syncfusion.com",
    url="https://www.syncfusion.com/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
