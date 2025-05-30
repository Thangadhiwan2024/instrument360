from v1.instruments.smu.hal import SMU, ConnectionState, PulseSourceMode
import pyvisa

class RS_NGU401(SMU):
    def __init__(self, instrument_address: str):
        super().__init__(instrument_address)
        rm = pyvisa.ResourceManager()
        self.instrument = rm.open_resource(instrument_address)

    def Abort(self, channel: str) -> None:
        print(f"Aborting operation on channel {channel}")
        self.instrument.write(f"ABORt")

    def Close(self, channel: str) -> None:
        self.instrument.write(f"INST:SEL {channel}; *RST")
        self.instrument.write("SYST:LOC")

    def ConnectDisconnectOutput(self, channel: str, state: ConnectionState = ConnectionState.Disconnect) -> None:
        if state == ConnectionState.Connect:
            self.instrument.write(f"OUTP {channel}, ON")
        else:
            self.instrument.write(f"OUTP {channel}, OFF")

    def SetOverCurrentProtection(self, channel: str, enable_ocp: bool = True, over_current_protection: float = 0.1) -> None:
        self.instrument.write(f"CURR:PROT {int(enable_ocp)}")
        self.instrument.write(f"CURR:PROT:LEV {over_current_protection}")

    def SetOverVoltageProtection(self, channel: str, enable_ovp: bool = True, over_voltage_protection: float = 10) -> None:
        self.instrument.write(f"VOLT:PROT {int(enable_ovp)}")
        self.instrument.write(f"VOLT:PROT:LEV {over_voltage_protection}")

    def SetPulseSourceMode(self, channel: str, pulse_mode: PulseSourceMode = PulseSourceMode.Pulse_Voltage) -> None:
        if pulse_mode == PulseSourceMode.Pulse_Voltage:
            self.instrument.write(f"SOUR{channel}:FUNC:MODE VOLT")
        elif pulse_mode == PulseSourceMode.Pulse_Current:
            self.instrument.write(f"SOUR{channel}:FUNC:MODE CURR")

    def SetPulseTimings(self, channel: str, pulse_period: float = 50, pulse_width: float = 25) -> None:
        if not 50e-6 <= pulse_period <= 100000:
            raise ValueError("Pulse period must be between 50 μs and 100000 s.")
        if not 50e-6 <= pulse_width <= 100000:
            raise ValueError("Pulse width must be between 50 μs and 100000 s.")
        
        self.instrument.write(f"CHANnel{channel}:PULSe:PERiod {pulse_period}")
        self.instrument.write(f"CHANnel{channel}:PULSe:WIDth {pulse_width}")