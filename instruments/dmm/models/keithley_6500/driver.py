from v1.abstract_class.HAL_DMM import DMM
import pyvisa

class keithley_6500(DMM):
    def __init__(self, instrument_address: str):
        super().__init__(instrument_address)
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(instrument_address)

    def StopMeasurement(self, channel: str) -> None:
        self.instrument.write(f"ABORt")

    def TerminateSession(self, channel: str) -> None:
        self.instrument.write(f"*RST;*CLS")

    def SetNPLC(self, channel: str, nplc: float) -> None:
        self.instrument.write(f"SENS:{channel}:NPLC {nplc}")

    def ToggleDisplay(self, state: bool) -> None:
        display_state = "ON" if state else "OFF"
        self.instrument.write(f"DISPlay:ENABle {display_state}")

    def ConfigureMeasurement(self, channel: str, measurement_function: str, range: float, resolution: float) -> None:
        self.instrument.write(f"CONF:{measurement_function} {channel}, {range}, {resolution}")

    def SetupMultiPointTrigger(self, channel: str, trigger_count: int, trigger_delay: float) -> None:
        self.instrument.write(f"TRIG:{channel}:COUN {trigger_count}")
        self.instrument.write(f"TRIG:{channel}:DEL {trigger_delay}")