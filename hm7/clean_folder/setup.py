from setuptools import setup, find_packages

entry_point = (
      'clean-folder = clean_folder.clean:main'
)

setup(name="clean_folder",
      version="0.1",
      description="clean_folder",
      author="Panpukha Oleksii",
      packages=find_packages(),
      entry_points={'console_scripts': [entry_point]}
    
)