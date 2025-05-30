from typing import List, Optional, Any
from pydantic import BaseModel

class AbortRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class AbortResponse(BaseModel):
    status: str
    message: Optional[str] = None

class CloseRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    operation: OperationMode

class CloseResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ConfigureBurstModeRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    enable_burst_mode: bool
    burst_phase: float
    burst_cycle: int
    burst_period: float
    trigger_source: TriggerSource
    additional_input: Any
    burst_mode: BurstMode
    gate_polarity: GatePolarity

class ConfigureBurstModeResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetHighLowLevelRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    value_high_in_v: float
    value_low_in_v: float

class SetHighLowLevelResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetOutputPolarityRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    output_polarity: str

class SetOutputPolarityResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetPulseDelayRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    pulse_delay_unit: PulseDelayUnit
    pulse_delay_value: float

class SetPulseDelayResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetPulseDutyCycleRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    duty_cycle: float

class SetPulseDutyCycleResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ConfigurePulseWaveformRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    leading_edge_time: float
    trailing_edge_time: float
    pulse_width: float
    pulse_period: float

class ConfigurePulseWaveformResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetRampWaveformRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    percentage: float

class SetRampWaveformResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetSquareWaveformRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    duty_cycle: float

class SetSquareWaveformResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetStandardWaveformRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    dc_offset: float
    frequency: float
    start_phase: float
    waveform: Waveform
    amplitude: float
    additional_input: Any

class SetStandardWaveformResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ConfigureFrequencySweepRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    power_array: List[float]
    dwell_time_array: List[float]
    frequency_array: List[float]

class ConfigureFrequencySweepResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ConfigureChannelTrackingRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    track_mode: TrackMode
    source_channel: SourceChannel

class ConfigureChannelTrackingResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetTriggerSlopeRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    trigger_slope: TriggerSlope

class SetTriggerSlopeResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetTriggerSourceRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    trigger_source: TriggerSource

class SetTriggerSourceResponse(BaseModel):
    status: str
    message: Optional[str] = None

class DisableChannelOutputRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class DisableChannelOutputResponse(BaseModel):
    status: str
    message: Optional[str] = None

class EnableChannelOutputRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class EnableChannelOutputResponse(BaseModel):
    status: str
    message: Optional[str] = None

class InitRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    fgen_type: str
    operation: OperationMode

class InitResponse(BaseModel):
    status: str
    message: Optional[str] = None

class InitiateRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class InitiateResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ResetRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class ResetResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SendSoftwareTriggerRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

class SendSoftwareTriggerResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetLoadImpedanceRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    load_impedance: float

class SetLoadImpedanceResponse(BaseModel):
    status: str
    message: Optional[str] = None

class SetOutputImpedanceRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str
    impedance: float

class SetOutputImpedanceResponse(BaseModel):
    status: str
    message: Optional[str] = None