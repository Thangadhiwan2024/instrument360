import nidcpower
from v1.instruments.smu.hal import SMU, ConnectionState

class NISmuController(SMU):
    def __init__(self, instrument_address: str):
        super().__init__(instrument_address)
        try:
            self.instrument_address = instrument_address
            self.instrument = nidcpower.Session(resource_name=self.instrument_address)
        except Exception as e:
            raise Exception(f"Failed to initialize session: {e}")

    def Init(self, channel: str) -> None:
        try:
            self.instrument.initiate()
        except Exception as e:
            raise Exception(f"Initialization failed: {e}")

    def Close(self, channel: str) -> None:
        try:
            self.instrument.close()
        except Exception as e:
            raise Exception(f"Closing session failed: {e}")

    def Abort(self, channel: str) -> None:
        try:
            self.instrument.abort()
        except Exception as e:
            raise Exception(f"Abort failed: {e}")

    def ConnectDisconnectOutput(self, channel: str, state: ConnectionState = ConnectionState.Disconnect) -> None:
        try:
            self.instrument.channels[channel].output_enabled = (state == ConnectionState.Connect)
        except Exception as e:
            raise Exception(f"Output connection toggle failed: {e}")

    def SetCurrentLevel(self, channel: str, current_level: float = 0.00001) -> None:
        try:
            self.instrument.channels[channel].current_level_autorange = True
            self.instrument.channels[channel].current_level = current_level
        except Exception as e:
            raise Exception(f"Set current level failed: {e}")

    def SetVoltageLevel(self, channel: str, voltage_level: float = 2) -> None:
        try:
            self.instrument.channels[channel].voltage_level_autorange = True
            self.instrument.channels[channel].voltage_level = voltage_level
        except Exception as e:
            raise Exception(f"Set voltage level failed: {e}")

    def SetCurrentLimit(self, channel: str, current_limit: float = 0.1) -> None:
        try:
            self.instrument.channels[channel].current_limit = current_limit
        except Exception as e:
            raise Exception(f"Set current limit failed: {e}")

    def SetVoltageLimit(self, channel: str, voltage_limit: float = 2) -> None:
        try:
            self.instrument.channels[channel].voltage_limit = voltage_limit
        except Exception as e:
            raise Exception(f"Set voltage limit failed: {e}")

    def GetCurrentMeasurement(self, channel: str):
        try:
            return [self.instrument.channels[channel].measure(nidcpower.MeasurementTypes.CURRENT)]
        except Exception as e:
            raise Exception(f"Current measurement failed: {e}")

    def GetVoltageMeasurement(self, channel: str):
        try:
            return [self.instrument.channels[channel].measure(nidcpower.MeasurementTypes.VOLTAGE)]
        except Exception as e:
            raise Exception(f"Voltage measurement failed: {e}")


    def Reset(self, channel: str) -> None:
        try:
            self.instrument.reset()
        except Exception as e:
            raise Exception(f"Device reset failed: {e}")



import time

# === CONFIGURATION ===
instrument_address = "PXI1Slot5"  # Replace with your actual SMU resource string
channel = "1"  # Replace with your actual channel name (e.g., "0", "1")

# === SETUP & RUN ===
if __name__ == "__main__":
    try:
        smu = NISmuController(instrument_address)

        # # Set source mode to VOLTAGE
        smu.SetSourceMode(channel, "DC_VOLTAGE")
        time.sleep(10)

        # # Set voltage level to 0.5 V and configure limit
        # smu.SetVoltageLevel(channel, voltage_level=0.5)
        # smu.SetCurrentLimit(channel, current_limit=0.01)  # Optional: current limit

        # # Enable output
        # smu.ConnectDisconnectOutput(channel, state=ConnectionState.Connect)

        # # Initialize the session


        # Optional: Read back measurements
        # voltage = smu.GetVoltageMeasurement(channel)
        # current = smu.GetCurrentMeasurement(channel)
        # print(f"Voltage Measured: {voltage}")
        # print(f"Current Measured: {current}")

        # # Stop sourcing
        # smu.Abort(channel)
        smu.SetSourceMode(channel, "DC_CURRENT")
        smu.Init(channel)

        # print(f"Sourcing 0.5 V on channel {channel} for 10 seconds...")
        time.sleep(10)
        # print(f"Output toggled on channel {channel}")
        # smu.ConnectDisconnectOutput(channel, state=ConnectionState.Disconnect)

    except Exception as e:
        print(f"Error during SMU operation: {e}")
    finally:
        try:
            smu.Close(channel)
        except:
            pass

