from enum import Enum
from typing import List, Optional, Any

class ConnectionState(str, Enum):
    Connect = "Connect"
    Disconnect = "Disconnect"

class PulseSourceMode(str, Enum):
    Pulse_Voltage = "Pulse Voltage"
    Pulse_Current = "Pulse Current"

class SenseMode(str, Enum):
    Local = "Local"
    Remote = "Remote"

class SourceMode(str, Enum):
    Voltage = "Voltage"
    Current = "Current"

class SMU:
    def __init__(self, instrument_address: str) -> None:
        """Initializes the SMU with the given instrument address."""
        self.instrument_address = instrument_address
        

    def Abort(self, channel: str) -> None:
        """Terminates the session for the SMU by halting any ongoing operations and resetting the session to a safe state."""
        pass

    def Close(self, channel: str) -> None:
        """Ends the session for the SMU by releasing the communication channel and freeing resources."""
        pass

    def ConnectDisconnectOutput(self, channel: str, state: ConnectionState = ConnectionState.Disconnect) -> None:
        """Connects or disconnects the output of the specified SMU channel."""
        pass

    def SetOverCurrentProtection(self, channel: str, enable_ocp: bool = True, over_current_protection: float = 0.1) -> None:
        """Configures over-current protection (OCP) for the specified channel."""
        pass

    def SetOverVoltageProtection(self, channel: str, enable_ovp: bool = True, over_voltage_protection: float = 10) -> None:
        """Configures over-voltage protection (OVP) for the specified channel."""
        pass

    def SetPulseSourceMode(self, channel: str, pulse_mode: PulseSourceMode = PulseSourceMode.Pulse_Voltage) -> None:
        """Configures the pulse source mode for the specified channel."""
        pass

    def SetPulseTimings(self, channel: str, pulse_period: float = 50, pulse_width: float = 25) -> None:
        """Configures the pulse period and pulse width for the specified channel."""
        pass

    def SetSenseMode(self, channel: str, sense: SenseMode = SenseMode.Local) -> None:
        """Configures the sense mode for the specified channel."""
        pass

    def SetSourceMode(self, channel: str, dc_source_mode: SourceMode = SourceMode.Voltage) -> None:
        """Configures the source mode for the specified channel."""
        pass

    def SetSourceDelay(self, channel: str, enable_source_delay: bool = False, source_delay: float = 0.1) -> None:
        """Sets the source delay time for the specified channel."""
        pass

    def ToggleOutputState(self, channel: str, state: bool = True) -> None:
        """Enables or disables the output for the specified channel."""
        pass

    def Init(self, channel: str) -> None:
        """Initializes the session for the SMU by establishing communication."""
        pass

    def Initiate(self, channel: str) -> None:
        """Initiates the session for the specified channel."""
        pass

    def GetCurrentMeasurement(self, channel: str) -> List[Any]:
        """Measures and returns the current for the specified channel."""
        pass

    def GetVoltageMeasurement(self, channel: str) -> List[Any]:
        """Measures and returns the voltage for the specified channel."""
        pass

    def Reset(self, channel: str) -> None:
        """Resets the instrument settings to the factory or default state."""
        pass

    def SetCurrentParameters(self, channel: str, current_level: float = 0.1, voltage_limit: float = 2, current_level_range: float = 0.1, voltage_limit_range: float = 6, source_delay: float = 0.1) -> None:
        """Configures the current level and voltage limit for the specified channel."""
        pass

    def SetCurrentLimit(self, channel: str, current_limit: float = 0.1) -> None:
        """Sets the maximum allowable current for the specified channel."""
        pass

    def SetCurrentLimitRange(self, channel: str, current_limit_range: float = 0.1, auto_range: bool = False) -> None:
        """Defines the permissible range for the current limit for the specified channel."""
        pass

    def SetCurrentLevel(self, channel: str, current_level: float = 0.1) -> None:
        """Configures the desired current level for the specified channel."""
        pass

    def SetCurrentRange(self, channel: str, current_level_range: float = 0.1, auto_range: bool = False) -> None:
        """Sets the permissible range for the current level for the specified channel."""
        pass

    def SetVoltageLimit(self, channel: str, voltage_limit: float = 2) -> None:
        """Sets the maximum allowable voltage for the specified channel."""
        pass

    def SetVoltageLimitRange(self, channel: str, voltage_limit_range: float = 6, auto_range: bool = False) -> None:
        """Defines the permissible range for the voltage limit for the specified channel."""
        pass

    def SetVoltageLevel(self, channel: str, voltage_level: float = 2) -> None:
        """Configures the desired voltage level for the specified channel."""
        pass

    def SetVoltageRange(self, channel: str, voltage_level_range: float = 6, auto_range: bool = False) -> None:
        """Sets the voltage range for the specified channel."""
        pass

    def SetPulseBaseCurrentLimit(self, channel: str, pulse_current_limit: float = 0.01) -> None:
        """Configures the limit for the pulse base current for the specified channel."""
        pass

    def SetPulseBaseCurrentLevel(self, channel: str, pulse_current_level: float = 0.1) -> None:
        """Sets the desired pulse base current level for the specified channel."""
        pass

    def SetPulseBaseVoltageLimit(self, channel: str, pulse_voltage_limit: float = 0.1) -> None:
        """Configures the maximum allowable pulse base voltage limit for the specified channel."""
        pass

    def SetPulseBaseVoltageLevel(self, channel: str, pulse_voltage_level: float = 0.2) -> None:
        """Sets the desired pulse base voltage level for the specified channel."""
        pass

    def SetPulseCurrentLimit(self, channel: str, pulse_current_limit: float = 0.1) -> None:
        """Sets the pulse current limit for the specified channel."""
        pass

    def SetPulseCurrentLimitRange(self, channel: str, pulse_current_limit_range: float = 0.1, auto_range: bool = False) -> None:
        """Sets the pulse current limit range for the specified channel."""
        pass

    def SetPulseCurrentLevel(self, channel: str, pulse_current_level: float = 0.1) -> None:
        """Sets the pulse current level for the specified channel."""
        pass

    def SetPulseCurrentLevelRange(self, channel: str, pulse_current_level_range: float, auto_range: bool = False) -> None:
        """Sets the pulse current level range for the specified channel."""
        pass

    def SetPulseVoltageLimit(self, channel: str, pulse_voltage_limit: float = 3) -> None:
        """Sets the pulse voltage limit for the specified channel."""
        pass

    def SetPulseVoltageLimitRange(self, channel: str, pulse_voltage_limit_range: float = 3, auto_range: bool = False) -> None:
        """Sets the pulse voltage limit range for the specified channel."""
        pass

    def SetPulseVoltageLevel(self, channel: str, pulse_voltage_level: float = 1) -> None:
        """Sets the pulse voltage level for the specified channel."""
        pass

    def SetPulseVoltageLevelRange(self, channel: str, pulse_voltage_level_range: float = 3, auto_range: bool = False) -> None:
        """Sets the pulse voltage level range for the specified channel."""
        pass
