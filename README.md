    Huawei Nova 5T Smartphone Class
This Python project defines a class representing a Huawei Nova 5T Smartphone. It demonstrates encapsulation, inheritance, and polymorphism.

    Features
Attributes: Model, color, storage, battery capacity, camera features.

Methods: Display phone details, manage storage, and show specific features.

Encapsulation: Private storage with getter/setter methods.

Inheritance & Polymorphism: Subclass HuaweiNova5T extends Smartphone and overrides features.

Installation
Ensure Python 3.x is installed.

Clone the repository or copy the code into a Python file.

    Run the Python file.

git clone https://github.com/yourusername/huawei-nova-5t.git
cd huawei-nova-5t
python huawei_nova_5t.py

     Usage

    # Create a Huawei Nova 5T object
huawei_nova_5t = HuaweiNova5T("Huawei Nova 5T", "Midnight Black", 128, 3750, "48MP + 16MP + 2MP")

    # Display phone details
print(huawei_nova_5t.phone_details())

    # Display phone features
print(huawei_nova_5t.display_features())

    # Modify storage
huawei_nova_5t.set_storage(256)
Concepts Demonstrated
Encapsulation: Private __storage attribute with getter/setter methods.

Inheritance: HuaweiNova5T inherits from Smartphone.

Polymorphism: display_features() is overridden in the subclass.

    License
This project is licensed under the MIT License.

