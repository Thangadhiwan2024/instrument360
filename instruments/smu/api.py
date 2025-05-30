from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum
from HAL.v1.utils.driver_manager import DriverManager  # Using absolute import

router = APIRouter(prefix="/smu", tags=["smu"])

# Enums matching the HAL_SMU class
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

# Base model for common parameters
class SMUBaseRequest(BaseModel):
    instrument_name: str
    instrument_address: str
    channel: str

# Request models for each endpoint
class ConnectDisconnectRequest(SMUBaseRequest):
    state: ConnectionState = ConnectionState.Disconnect

class ProtectionRequest(SMUBaseRequest):
    enable: bool = True
    protection_value: float

class PulseSourceRequest(SMUBaseRequest):
    pulse_mode: PulseSourceMode = PulseSourceMode.Pulse_Voltage

class PulseTimingsRequest(SMUBaseRequest):
    pulse_period: float = 50
    pulse_width: float = 25

class SenseModeRequest(SMUBaseRequest):
    sense: SenseMode = SenseMode.Local

class SourceModeRequest(SMUBaseRequest):
    dc_source_mode: SourceMode = SourceMode.Voltage

class SourceDelayRequest(SMUBaseRequest):
    enable_source_delay: bool = False
    source_delay: float = 0.1

class OutputStateRequest(SMUBaseRequest):
    state: bool = True

class CurrentParametersRequest(SMUBaseRequest):
    current_level: float = 0.1
    voltage_limit: float = 2
    current_level_range: float = 0.1
    voltage_limit_range: float = 6
    source_delay: float = 0.1

class LimitRequest(SMUBaseRequest):
    limit_value: float

class RangeRequest(SMUBaseRequest):
    range_value: float
    auto_range: bool = False

class LevelRequest(SMUBaseRequest):
    level_value: float

driver_manager = DriverManager()
# Endpoints
@router.post("/abort")
async def abort(request: SMUBaseRequest):
    """Abort SMU operations"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.Abort(request.channel)
    return {"message": "Operation aborted successfully"}

@router.post("/close")
async def close(request: SMUBaseRequest):
    """Close SMU connection"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.Close(request.channel)
    return {"message": "Connection closed successfully"}

@router.post("/connect-disconnect")
async def connect_disconnect(request: ConnectDisconnectRequest):
    """Connect or disconnect SMU output"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.ConnectDisconnectOutput(request.channel, request.state)
    return {"message": f"Output {request.state.value}ed successfully"}

@router.post("/over-current-protection")
async def set_over_current_protection(request: ProtectionRequest):
    """Set over-current protection"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetOverCurrentProtection(request.channel, request.enable, request.protection_value)
    return {"message": f"Over-current protection {'enabled' if request.enable else 'disabled'} at {request.protection_value}A"}

@router.post("/over-voltage-protection")
async def set_over_voltage_protection(request: ProtectionRequest):
    """Set over-voltage protection"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetOverVoltageProtection(request.channel, request.enable, request.protection_value)
    return {"message": f"Over-voltage protection {'enabled' if request.enable else 'disabled'} at {request.protection_value}V"}

@router.post("/pulse-source-mode")
async def set_pulse_source_mode(request: PulseSourceRequest):
    """Set pulse source mode"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseSourceMode(request.channel, request.pulse_mode)
    return {"message": f"Pulse source mode set to {request.pulse_mode.value}"}

@router.post("/pulse-timings")
async def set_pulse_timings(request: PulseTimingsRequest):
    """Set pulse timings"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseTimings(request.channel, request.pulse_period, request.pulse_width)
    return {"message": f"Pulse timings set: period={request.pulse_period}ms, width={request.pulse_width}ms"}

@router.post("/sense-mode")
async def set_sense_mode(request: SenseModeRequest):
    """Set sense mode"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetSenseMode(request.channel, request.sense)
    return {"message": f"Sense mode set to {request.sense.value}"}

@router.post("/source-mode")
async def set_source_mode(request: SourceModeRequest):
    """Set source mode"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetSourceMode(request.channel, request.dc_source_mode)
    return {"message": f"Source mode set to {request.dc_source_mode.value}"}

@router.post("/source-delay")
async def set_source_delay(request: SourceDelayRequest):
    """Set source delay"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetSourceDelay(request.channel, request.enable_source_delay, request.source_delay)
    return {"message": f"Source delay {'enabled' if request.enable_source_delay else 'disabled'} at {request.source_delay}s"}

@router.post("/output-state")
async def toggle_output_state(request: OutputStateRequest):
    """Toggle output state"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.ToggleOutputState(request.channel, request.state)
    return {"message": f"Output {'enabled' if request.state else 'disabled'}"}

@router.post("/init")
async def init(request: SMUBaseRequest):
    """Initialize SMU"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.Init(request.channel)
    return {"message": "SMU initialized successfully"}

@router.post("/initiate")
async def initiate(request: SMUBaseRequest):
    """Initiate SMU session"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.Initiate(request.channel)
    return {"message": "SMU session initiated successfully"}

@router.get("/current-measurement")
async def get_current_measurement(request: SMUBaseRequest):
    """Get current measurement"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    result = smu.GetCurrentMeasurement(request.channel)
    return {"current": result, "units": "A"}

@router.get("/voltage-measurement")
async def get_voltage_measurement(request: SMUBaseRequest):
    """Get voltage measurement"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    result = smu.GetVoltageMeasurement(request.channel)
    return {"voltage": result, "units": "V"}

@router.post("/reset")
async def reset(request: SMUBaseRequest):
    """Reset SMU"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.Reset(request.channel)
    return {"message": "SMU reset successfully"}

@router.post("/current-parameters")
async def set_current_parameters(request: CurrentParametersRequest):
    """Set current parameters"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetCurrentParameters(
        request.channel,
        request.current_level,
        request.voltage_limit,
        request.current_level_range,
        request.voltage_limit_range,
        request.source_delay
    )
    return {"message": "Current parameters set successfully"}

@router.post("/current-limit")
async def set_current_limit(request: LimitRequest):
    """Set current limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetCurrentLimit(request.channel, request.limit_value)
    return {"message": f"Current limit set to {request.limit_value}A"}

@router.post("/current-limit-range")
async def set_current_limit_range(request: RangeRequest):
    """Set current limit range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetCurrentLimitRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Current limit range set to {request.range_value}A"}

@router.post("/current-level")
async def set_current_level(request: LevelRequest):
    """Set current level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetCurrentLevel(request.channel, request.level_value)
    return {"message": f"Current level set to {request.level_value}A"}

@router.post("/current-range")
async def set_current_range(request: RangeRequest):
    """Set current range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetCurrentRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Current range set to {request.range_value}A"}

@router.post("/voltage-limit")
async def set_voltage_limit(request: LimitRequest):
    """Set voltage limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetVoltageLimit(request.channel, request.limit_value)
    return {"message": f"Voltage limit set to {request.limit_value}V"}

@router.post("/voltage-limit-range")
async def set_voltage_limit_range(request: RangeRequest):
    """Set voltage limit range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetVoltageLimitRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Voltage limit range set to {request.range_value}V"}

@router.post("/voltage-level")
async def set_voltage_level(request: LevelRequest):
    """Set voltage level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetVoltageLevel(request.channel, request.level_value)
    return {"message": f"Voltage level set to {request.level_value}V"}

@router.post("/voltage-range")
async def set_voltage_range(request: RangeRequest):
    """Set voltage range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetVoltageRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Voltage range set to {request.range_value}V"}

@router.post("/pulse-base-current-limit")
async def set_pulse_base_current_limit(request: LimitRequest):
    """Set pulse base current limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseBaseCurrentLimit(request.channel, request.limit_value)
    return {"message": f"Pulse base current limit set to {request.limit_value}A"}

@router.post("/pulse-base-current-level")
async def set_pulse_base_current_level(request: LevelRequest):
    """Set pulse base current level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseBaseCurrentLevel(request.channel, request.level_value)
    return {"message": f"Pulse base current level set to {request.level_value}A"}

@router.post("/pulse-base-voltage-limit")
async def set_pulse_base_voltage_limit(request: LimitRequest):
    """Set pulse base voltage limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseBaseVoltageLimit(request.channel, request.limit_value)
    return {"message": f"Pulse base voltage limit set to {request.limit_value}V"}

@router.post("/pulse-base-voltage-level")
async def set_pulse_base_voltage_level(request: LevelRequest):
    """Set pulse base voltage level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseBaseVoltageLevel(request.channel, request.level_value)
    return {"message": f"Pulse base voltage level set to {request.level_value}V"}

@router.post("/pulse-current-limit")
async def set_pulse_current_limit(request: LimitRequest):
    """Set pulse current limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseCurrentLimit(request.channel, request.limit_value)
    return {"message": f"Pulse current limit set to {request.limit_value}A"}

@router.post("/pulse-current-limit-range")
async def set_pulse_current_limit_range(request: RangeRequest):
    """Set pulse current limit range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseCurrentLimitRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Pulse current limit range set to {request.range_value}A"}

@router.post("/pulse-current-level")
async def set_pulse_current_level(request: LevelRequest):
    """Set pulse current level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseCurrentLevel(request.channel, request.level_value)
    return {"message": f"Pulse current level set to {request.level_value}A"}

@router.post("/pulse-current-level-range")
async def set_pulse_current_level_range(request: RangeRequest):
    """Set pulse current level range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseCurrentLevelRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Pulse current level range set to {request.range_value}A"}

@router.post("/pulse-voltage-limit")
async def set_pulse_voltage_limit(request: LimitRequest):
    """Set pulse voltage limit"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseVoltageLimit(request.channel, request.limit_value)
    return {"message": f"Pulse voltage limit set to {request.limit_value}V"}

@router.post("/pulse-voltage-limit-range")
async def set_pulse_voltage_limit_range(request: RangeRequest):
    """Set pulse voltage limit range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseVoltageLimitRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Pulse voltage limit range set to {request.range_value}V"}

@router.post("/pulse-voltage-level")
async def set_pulse_voltage_level(request: LevelRequest):
    """Set pulse voltage level"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseVoltageLevel(request.channel, request.level_value)
    return {"message": f"Pulse voltage level set to {request.level_value}V"}

@router.post("/pulse-voltage-level-range")
async def set_pulse_voltage_level_range(request: RangeRequest):
    """Set pulse voltage level range"""
    smu = driver_manager.get_instance("smu", request.instrument_name, request.instrument_address)
    smu.SetPulseVoltageLevelRange(request.channel, request.range_value, request.auto_range)
    return {"message": f"Pulse voltage level range set to {request.range_value}V"}