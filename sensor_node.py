from abc import ABC, abstractmethod #

# 1. Abstract Data Type (ADT) / Abstraction
class AbstractSensor(ABC): #
    # 2. Class Attribute - Keep track of total registered sensors in the network
    total_active_sensors = 0 
    NETWORK_SUFFIX = "@smartcity.hk" # Similar to EMAIL_SUFFIX in the lecture notes

    def __init__(self, sensor_id, location): #
        self.sensor_id = sensor_id
        self.location = location
        # 3. Encapsulation - Hide internal state, disallow direct modification of battery level from outside
        self._battery_level = 100.0  
        self._is_online = True
        
        # Increment class attribute by 1 each time an object is initialized
        AbstractSensor.total_active_sensors += 1

    # 4. Getter and Setter methods - Standardize data access
    def get_battery_level(self):
        return self._battery_level

    def set_battery_level(self, level):
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            print("Error: Battery level must be between 0 and 100.")

    # 5. Abstract Method - Force subclasses to implement their own signal processing logic
    @abstractmethod
    def process_signal(self):
        pass

    # 6. Class Method - Used to operate on class-level attributes
    @classmethod
    def get_network_status(cls):
        return f"Total active sensors on network: {cls.total_active_sensors}"

    # 7. Static Method - Logically belongs to this class, but doesn't need to access instance or class data
    # e.g., A general signal conversion utility function (A/D conversion)
    @staticmethod
    def analog_to_digital(raw_analog_voltage):
        # Simulate converting a 0-5V analog voltage signal to a 0-1023 digital signal
        return int((raw_analog_voltage / 5.0) * 1023)

    # 8. Magic Methods - Customize object behavior
    def __str__(self): # Define the string output format of the object
        return f"[Sensor {self.sensor_id}] at {self.location} | Battery: {self._battery_level}%"

    def __eq__(self, other): # Define if two sensors are "equal" (e.g., same ID means the same device)
        if isinstance(other, AbstractSensor):
            return self.sensor_id == other.sensor_id
        return False


# 9. Inheritance and Polymorphism
class AirQualitySensor(AbstractSensor):
    def __init__(self, sensor_id, location, target_gas):
        # Call the parent class's __init__
        super().__init__(sensor_id, location)
        self.target_gas = target_gas

    # Implement the abstract method defined by the parent class
    def process_signal(self):
        # Demonstration of polymorphism: different sensors process signals differently
        print(f"{self.sensor_id} is analyzing digital signal for {self.target_gas} concentration...")

class TrafficCamera(AbstractSensor):
    def __init__(self, sensor_id, location, resolution):
        super().__init__(sensor_id, location)
        self.resolution = resolution

    def process_signal(self):
        print(f"{self.sensor_id} is processing video feed at {self.resolution} resolution...")
