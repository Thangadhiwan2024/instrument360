from enum import Enum
from typing import Any, Optional

class Function(Enum):
    DC_VOLTS = "DC Volts"
    AC_VOLTS = "AC Volts"
    DC_CURRENT = "DC Current"
    AC_CURRENT = "AC Current"
    DIODE = "Diode"
    POWER_METER = "Power Meter"
    CAPACITANCE = "Capacitance"
    TEMPERATURE = "Temperature"
    FREQUENCY = "Frequency"
    TWO_WIRE_RESISTANCE = "2-Wire Resistance"
    FOUR_WIRE_RESISTANCE = "4 Wire Resistance"

class Display(Enum):
    ON = "ON"
    OFF = "OFF"

class Operation(Enum):
    CREATE_NEW_SESSION = "Create New Session"
    FETCH_EXISTING_SESSION = "Fetch Existing Session"
    CLOSE_AND_DESTROY = "Close & Destroy"
    DESTROY_DONT_CLOSE = "Destroy & Don't Close"

class TriggerSource(Enum):
    AUTO = "Auto"
    IMMEDIATE = "Immediate"
    EXTERNAL = "External"
    MANUAL = "Manual"
    BUS_SOURCE = "Bus/Source"

class Resolution(Enum):
    THREE_HALF = "3 1/2"
    FOUR_HALF = "4 1/2"
    FIVE_HALF = "5 1/2"
    SIX_HALF = "6 1/2"
    SEVEN_HALF = "7 1/2"
    EIGHT_HALF = "8 1/2"

class DMM:
    def __init__(self, instrument_address: str):
        self.instrument_address = instrument_address

    def StopMeasurement(self, Instrument_Address: str, Channel: str = "") -> None:
        """Stops the previously initiated measurement."""
        pass

    def TerminateSession(self, Instrument_Address: str, Channel: str = "", operation: Operation = Operation.CLOSE_AND_DESTROY) -> None:
        """Terminates the instrument session."""
        pass

    def SetNPLC(self, Instrument_Address: str, Channel: str = "", Function: Function = Function.DC_VOLTS, NPLC: float = 0.02) -> None:
        """Configures the number of Power Line Cycles (NPLC)."""
        pass

    def ConfigureMeasurement(self, Instrument_Address: str, Channel: str = "", Resolution_in_digits: Resolution = Resolution.EIGHT_HALF, Function: Function = Function.DC_VOLTS, Range: float = 0.02, Additional_info: Optional[Any] = None) -> None:
        """Sets up the measurement function, range, and resolution."""
        pass

    def ToggleDisplay(self, Instrument_Address: str, Channel: str = "", Display: Display = Display.ON) -> None:
        """Enables or disables the display on the DMM."""
        pass

    def SetupMultiPointTrigger(self, Instrument_Address: str, Channel: str = "", Trigger_Source: TriggerSource = TriggerSource.IMMEDIATE, Trigger_Count: int = 1, Sample_Count: int = 1, Sample_Interval: int = 0) -> None:
        """Configures the trigger source and counts for multipoint measurements."""
        pass

    def InitializeSession(self, Instrument_Address: str, Channel: str = "", Operation: Operation = Operation.CREATE_NEW_SESSION) -> None:
        """Initializes the session of the DMM."""
        pass

    def StartMeasurement(self, Instrument_Address: str, Channel: str = "") -> None:
        """Starts the DMM for measurements."""
        pass

    def ReadMultipleMeasurements(self, Instrument_Address: str, Channel: str = "") -> None:
        """Reads multiple measurements equal to the entered sample count."""
        pass

    def ReadSingleMeasurement(self, Instrument_Address: str, Channel: str = "") -> None:
        """Reads a single measurement."""
        pass

    def RestoreDefaults(self, Instrument_Address: str, Channel: str = "") -> None:
        """Restores the DMM to its default settings."""
        pass