from setuptools import find_packages, setup

package_name = 'delta_x_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TaoPeter',
    maintainer_email='taothienpeter@gmail.com',
    description='TODO: Package description',
    license='.vscode/',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driver_control = delta_x_rover.driver_control:main'
        ],
    },
)
