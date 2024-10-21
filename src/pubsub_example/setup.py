from setuptools import setup

package_name = 'pubsub_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='suzaku',
    maintainer_email='suzaku@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = pubsub_example.publisher_node:main',
            'subscriber_node = pubsub_example.subscriber_node:main'
        ],
    },
)
