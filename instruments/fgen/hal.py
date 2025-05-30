from enum import Enum
from typing import List, Any

class OperationMode(str, Enum):
    CLOSE_DESTROY = "Close & Destroy"
    DESTROY_DONT_CLOSE = "Destroy & Don't Close"

class TriggerSource(str, Enum):
    INTERNAL = "Internal"
    EXTERNAL = "External"
    MANUAL = "Manual"

class BurstMode(str, Enum):
    TRIGGERED = "Triggered"
    GATED = "Gated"

class GatePolarity(str, Enum):
    NORMAL = "Normal"
    INVERTED = "Inverted"

class PulseDelayUnit(str, Enum):
    SECONDS = "Seconds"
    RADIANS = "Radians"
    PERCENT = "Percent"
    DEGREE = "Degree"

class Waveform(str, Enum):
    SINE = "Sine"
    SQUARE = "Square"
    RAMP_UP = "Ramp Up"
    DC = "DC"
    NOISE = "Noise"
    TRIANGLE = "Triangle"
    PULSE = "Pulse"
    RAMP_DOWN = "Ramp Down"
    RAMP = "Ramp"

class TrackMode(str, Enum):
    ON = "ON"
    OFF = "OFF"
    INVERT = "Invert"

class SourceChannel(str, Enum):
    CHANNEL_1 = "1"
    CHANNEL_2 = "2"

class TriggerSlope(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"

class FGEN:
    def __init__(self, instrument_address: str):
        self.instrument_address = instrument_address

    def Abort(self, instrument_address: str, channel: str) -> None:
        """Stops the current operation on the specified channel(s)."""
        pass

    def Close(self, instrument_address: str, channel: str, operation: OperationMode = OperationMode.CLOSE_DESTROY) -> None:
        """Terminates the instrument session for the specified channel(s)."""
        pass

    def ConfigureBurstMode(self, instrument_address: str, channel: str, enable_burst_mode: bool = False, burst_phase: float = 0.0, burst_cycle: int = 1, burst_period: float = 0.0, trigger_source: TriggerSource = TriggerSource.INTERNAL, additional_input: Any = "", burst_mode: BurstMode = BurstMode.TRIGGERED, gate_polarity: GatePolarity = GatePolarity.NORMAL) -> None:
        """Sets up burst modulation for the specified channel(s)."""
        pass

    def SetHighLowLevel(self, instrument_address: str, channel: str, value_high_in_v: float = 0.5, value_low_in_v: float = -0.5) -> None:
        """Configures the high-level and low-level of the output signal."""
        pass

    def SetOutputPolarity(self, instrument_address: str, channel: str, output_polarity: str = "Normal") -> None:
        """Inverts the waveform relative to the offset voltage."""
        pass

    def SetPulseDelay(self, instrument_address: str, channel: str, pulse_delay_unit: PulseDelayUnit = PulseDelayUnit.SECONDS, pulse_delay_value: float = 0.0) -> None:
        """Configures the pulse delay value and unit."""
        pass

    def SetPulseDutyCycle(self, instrument_address: str, channel: str, duty_cycle: float = 50.00) -> None:
        """Configures the Duty Cycle of the Pulse waveform."""
        pass

    def ConfigurePulseWaveform(self, instrument_address: str, channel: str, leading_edge_time: float = 5E-9, trailing_edge_time: float = 5E-9, pulse_width: float = 0.0001, pulse_period: float = 0.001) -> None:
        """Sets up the parameters for the pulse waveform."""
        pass

    def SetRampWaveform(self, instrument_address: str, channel: str, percentage: float = 100.0) -> None:
        """Configures the Symmetry of the Ramp waveform."""
        pass

    def SetSquareWaveform(self, instrument_address: str, channel: str, duty_cycle: float = 50.00) -> None:
        """Configures the Duty Cycle of the Square waveform."""
        pass

    def SetStandardWaveform(self, instrument_address: str, channel: str, dc_offset: float = 0.0, frequency: float = 1000, start_phase: float = 0.0, waveform: Waveform = Waveform.SINE, amplitude: float = 0.10, additional_input: Any = "") -> None:
        """Configures the waveform shape for the specified channel(s)."""
        pass

    def ConfigureFrequencySweep(self, instrument_address: str, channel: str, power_array: List[float] = [], dwell_time_array: List[float] = [0.002], frequency_array: List[float] = [1000]) -> None:
        """Sets up the Frequency Sweep for the specified channel(s)."""
        pass

    def ConfigureChannelTracking(self, instrument_address: str, channel: str, track_mode: TrackMode = TrackMode.ON, source_channel: SourceChannel = SourceChannel.CHANNEL_1) -> None:
        """Sets up tracking mode for channels."""
        pass

    def SetTriggerSlope(self, instrument_address: str, channel: str, trigger_slope: TriggerSlope = TriggerSlope.POSITIVE) -> None:
        """Configures the polarity of the External Trigger terminal."""
        pass

    def SetTriggerSource(self, instrument_address: str, channel: str, trigger_source: TriggerSource = TriggerSource.SOFTWARE) -> None:
        """Configures the Trigger Source for the specified channel(s)."""
        pass

    def DisableChannelOutput(self, instrument_address: str, channel: str) -> None:
        """Turns off the output of the specified channel(s)."""
        pass

    def EnableChannelOutput(self, instrument_address: str, channel: str) -> None:
        """Turns on the output of the specified channel(s)."""
        pass

    def Init(self, instrument_address: str, channel: str, fgen_type: str = "", operation: OperationMode = OperationMode.CLOSE_DESTROY) -> None:
        """Starts the session of the Function Generator."""
        pass

    def Initiate(self, instrument_address: str, channel: str) -> None:
        """Begins the specified channel(s) of the Function Generator."""
        pass

    def Reset(self, instrument_address: str, channel: str) -> None:
        """Resets the specified Function Generator."""
        pass

    def SendSoftwareTrigger(self, instrument_address: str, channel: str) -> None:
        """Sends a software trigger to the specified Function Generator."""
        pass

    def SetLoadImpedance(self, instrument_address: str, channel: str, load_impedance: float = 50.0) -> None:
        """Configures the load impedance for the specified channel(s)."""
        pass

    def SetOutputImpedance(self, instrument_address: str, channel: str, impedance: float = 50.0) -> None:
        """Configures the output impedance for the specified channel(s)."""
        pass