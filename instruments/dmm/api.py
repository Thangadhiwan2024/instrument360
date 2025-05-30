from pydantic import BaseModel
from typing import Optional, Any
from enum import Enum

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

class StopMeasurementRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""

class StopMeasurementResponse(BaseModel):
    status: str
    message: Optional[str] = None

class TerminateSessionRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    operation: Operation

class TerminateSessionResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetNPLCRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    Function: Function
    NPLC: float = 0.02

class SetNPLCResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ConfigureMeasurementRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    Resolution_in_digits: Resolution
    Function: Function
    Range: float = 0.02
    Additional_info: Optional[Any] = None

class ConfigureMeasurementResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ToggleDisplayRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    Display: Display

class ToggleDisplayResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetupMultiPointTriggerRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    Trigger_Source: TriggerSource
    Trigger_Count: int = 1
    Sample_Count: int = 1
    Sample_Interval: int = 0

class SetupMultiPointTriggerResponse(BaseModel):
    status: str
    message: Optional[str] = None

class InitializeSessionRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""
    Operation: Operation

class InitializeSessionResponse(BaseModel):
    status: str
    message: Optional[str] = None

class StartMeasurementRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""

class StartMeasurementResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ReadMultipleMeasurementsRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""

class ReadMultipleMeasurementsResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ReadSingleMeasurementRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""

class ReadSingleMeasurementResponse(BaseModel):
    status: str
    message: Optional[str] = None

class RestoreDefaultsRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    Channel: str = ""

class RestoreDefaultsResponse(BaseModel):
    status: str
    message: Optional[str] = None