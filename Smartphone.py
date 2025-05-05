class Smartphone:
    def __init__(self, model, color, storage, battery_capacity):
        self.model = model  # Model of the phone (e.g., Huawei Nova 5T)
        self.color = color  # Color of the phone (e.g., Midnight Black)
        self.__storage = storage  # Storage (Private attribute for encapsulation)
        self.battery_capacity = battery_capacity  # Battery capacity in mAh

    def get_storage(self):
        return self.__storage
    def set_storage(self, new_storage):
        if new_storage > self.__storage:
            self.__storage = new_storage
            print(f"Storage updated to {new_storage}GB.")
        else:
            print("New storage must be greater than current storage.")

    def phone_details(self):
        return f"{self.model} ({self.color}) - {self.__storage}GB Storage, {self.battery_capacity}mAh battery"

    def display_features(self):
        return f"{self.model} features: 6.26-inch display, 48MP camera, Kirin 980 chipset."

class HuaweiNova5T(Smartphone):
    def __init__(self, model, color, storage, battery_capacity, camera_features):
        super().__init__(model, color, storage, battery_capacity)  # Inherits from Smartphone class
        self.camera_features = camera_features  # New attribute specific to Huawei Nova 5T
    def display_features(self):
        base_features = super().display_features()
        return f"{base_features} Camera: {self.camera_features}"

huawei_nova_5t = HuaweiNova5T("Huawei Nova 5T", "Midnight Black", 128, 3750, "48MP + 16MP + 2MP")

print(huawei_nova_5t.phone_details())

print(huawei_nova_5t.display_features())

print("Current storage:", huawei_nova_5t.get_storage())
huawei_nova_5t.set_storage(256)  # Update the storage
print("Updated storage:", huawei_nova_5t.get_storage())
