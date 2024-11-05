from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color


color_sensor = ColorSensor(Port.S1)

def checkColor(target_color, threshold=5):
    """
    Check if the color sensor reading is close to the target color.
    
    Parameters:
        target_color (Color): The target color to match.
        threshold (int): The acceptable threshold for closeness.
        
    Returns:
        bool: True if the color is close to the target color, False otherwise.
    """
    # Get the current color reading from the sensor
    current_color = color_sensor.color()
    
    # Check if the color matches the target within the specified threshold
    return current_color == target_color

