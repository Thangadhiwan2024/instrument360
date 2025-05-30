# Oscilloscope

An **Oscilloscope** is an essential electronic test instrument used to observe and analyze varying signal voltages over time. It plays a vital role in **semiconductor testing**, **circuit debugging**, and **signal integrity analysis**.

---

## **Key Features**

### **High Bandwidth and Sampling Rate**
- Captures high-speed signals accurately.
- Supports a wide range of frequencies from kHz to several GHz.

### **Real-Time Waveform Display**
- Provides visual representation of signal behavior in real time.
- Displays voltage vs. time for easy analysis of signal properties.

### **Advanced Triggering and Measurement**
- Enables precise signal capture with multiple trigger modes.
- Offers automatic measurements like rise time, frequency, and RMS voltage.

---

## **Applications**

### **Semiconductor Validation**
- Analyzes digital and analog signals in ICs and SoCs.
- Validates timing, noise margins, and voltage levels.

### **Circuit Debugging**
- Identifies faults in analog and digital circuits.
- Troubleshoots issues such as glitches, timing errors, and signal dropouts.

### **Signal Integrity Analysis**
- Assesses signal quality in high-speed communication systems.
- Detects signal distortions, jitter, and reflections.

---

## **Advantages**

### **Accurate Visualization of Signals**
- Helps in understanding circuit behavior with detailed waveform analysis.
- Enables engineers to detect even subtle anomalies in signal behavior.

### **Versatile Measurement Capabilities**
- Suitable for a wide range of electronic applications.
- Measures both periodic and non-periodic waveforms.

### **Data Storage and Connectivity**
- Supports waveform storage for offline analysis.
- Offers USB, LAN, or Wi-Fi connectivity for remote access and automation.

---

## **Abstract Methods**

### 1. `StopAcquisition`
#### Description
Halts any ongoing signal acquisition and transitions the oscilloscope to an idle state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 2. `AutoConfigure`
#### Description
Automatically adjusts the oscilloscope's settings based on the detected input signal.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 3. `SaveScreenCapture`
#### Description
Takes a snapshot of the oscilloscope's display and saves it as an image in the specified format and location.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | File Path | File Path | - | - |
| 4 | File Name | String | - | - |
| 5 | File Format | Enum | PNG, BMP, JPG, TIFF | - |
| 6 | Replace Existing File | Boolean | True, False | FALSE |

#### Output Parameters
None

### 4. `EndSession`
#### Description
Ends the current acquisition session and resets the oscilloscope to an idle state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 5. `SetAcquisitionType`
#### Description
Defines the acquisition type and, if applicable, sets the averaging count for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Acquisition Type | Enum | Sample, Peak Detect, Envelope, Average | Sample |
| 4 | Average Count | Integer | - | 16 |

#### Output Parameters
None

### 6. `SetBandwidthLimit`
#### Description
Adjusts the bandwidth limit for the specified channel(s) on the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Bandwidth | Double | - | 20MHz |

#### Output Parameters
None

### 7. `SetInputImpedance`
#### Description
Sets the input impedance for the specified channel(s) on the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Channel Impedance | Enum | - | 1M Ohms |

#### Output Parameters
None

### 8. `SetChannelLabel`
#### Description
Assigns a custom label to the waveform displayed for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Label Name | String | - | - |

#### Output Parameters
None

### 9. `SetLabelPosition`
#### Description
Positions the label for the specified channel(s) on the oscilloscope display.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Horizontal Position | Double | - | - |
| 4 | Vertical Position | Double | - | - |

#### Output Parameters
None

### 10. `SetContinuousMode`
#### Description
Configures the oscilloscope to operate in continuous acquisition mode or stop after a single acquisition.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Continuous Acquisition | Boolean | True, False | TRUE |

#### Output Parameters
None

### 11. `SetCursorFunctionality`
#### Description
Enables or disables cursor functionality and sets the cursor type for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Cursor State | Boolean | True, False | FALSE |
| 4 | Cursor Function | Enum | - | - |

#### Output Parameters
None

### 12. `SetCursorTracking`
#### Description
Defines the cursor tracking mode for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Cursor Mode | Enum | Independent, Track | - |

#### Output Parameters
None

### 13. `SetCursorParameters`
#### Description
Adjusts the positions and units for horizontal and vertical cursors.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | HBar Position 1 | Double | - | - |
| 4 | HBar Position 2 | Double | - | - |
| 5 | VBar Position 1 | Double | - | - |
| 6 | VBar Position 2 | Double | - | - |
| 7 | HBar Unit | Enum | Percent, Seconds, Hertz, Degrees | Percent |
| 8 | VBar Unit | Enum | Base, Percent, Seconds, Hertz, Degrees, Ampere, Voltage, Watt | Base |

#### Output Parameters
None

### 14. `SetCursorSource`
#### Description
Specifies the source for the cursor functionality based on the selected mode.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Cursor Source Mode | Enum | Same, Split | Same |
| 4 | Cursor 1 Source | String | - | - |
| 5 | Cursor 2 Source | String | - | - |

#### Output Parameters
None

### 15. `SetDelayMeasurement`
#### Description
Configures parameters for measuring delay between waveforms.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Search Direction | Enum | Forwards | - |
| 4 | Source Waveform Slope | Enum | Rising, Falling | Rising |
| 5 | Destination Waveform Slope | Enum | Rising, Falling | Rising |

#### Output Parameters
None

### 16. `SetEdgeTrigger`
#### Description
Configures the oscilloscope to trigger on a signal edge and sets the trigger parameters.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Level in V | Double | - | 1.000000 |
| 4 | Trigger Slope | Enum | Rising, Falling | Rising |

#### Output Parameters
None

### 17. `SetWaveformPoints`
#### Description
Defines the start and end points for waveform data acquisition.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Start Point | Integer | - | 1 |
| 4 | End Point | Integer | - | 2500 |

#### Output Parameters
None

### 18. `SetHorizontalPosition`
#### Description
Adjusts the horizontal position of the waveform on the oscilloscope display.

**Note:** This method depends on the time delay state of the instrument. Call **SetTimeDelay** API first to disable the time delay state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Position | Double | - | - |
| 4 | Unit | Enum | Percentage, Seconds | Percentage |

#### Output Parameters
None

### 19. `ToggleMeasurementDisplay`
#### Description
Enables or disables the display of measurement parameters on the oscilloscope's front panel.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Display? | Boolean | True, False | TRUE |
| 4 | Measurement Parameter | String | - | - |

#### Output Parameters
None

### 20. `SetMeasurementParameter`
#### Description
Configures the measurement parameter or variable for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Measurement Function | Enum | - | - |
| 4 | Measurement Parameter | String | - | - |
| 5 | Destination Channel | Integer | - | - |

#### Output Parameters
None

### 21. `ToggleMeasurementStatistics`
#### Description
Enables or disables the statistics mode for measurements.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Measurement Statistics? | Boolean | True, False | TRUE |

#### Output Parameters
None

### 22. `SetProbeScaling`
#### Description
Adjusts the probe attenuation factor for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Probe Attenuation | Double | - | 1.000000 |

#### Output Parameters
None

### 23. `SetRecordLength`
#### Description
Specifies the number of data points to record during waveform acquisition.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Record Length | Double | - | 10000 |

#### Output Parameters
None

### 24. `SetReferenceCalculation`
#### Description
Defines the method for calculating reference levels.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Ref Level Calc Method | Enum | Auto Select, Histogram, Min/Max | Auto Select |

#### Output Parameters
None

### 25. `SetReferenceLevels`
#### Description
Configures reference levels for waveform measurements, including high, low, and mid-levels.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | High Ref | Double | - | 9 |
| 4 | Low Ref | Double | - | 1 |
| 5 | Mid Ref | Double | - | 5 |
| 6 | Second Source Mid Ref | Double | - | 5 |
| 7 | Units | Enum | Percentage, Volts | Percentage |

#### Output Parameters
None

### 26. `SetSamplingRate`
#### Description
Specifies the number of samples to capture per second during acquisition.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Sample Rate | Double | - | - |

#### Output Parameters
None

### 27. `SetSamplingMode`
#### Description
Defines the sampling mode (real-time or equivalent time) for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Sampling Mode | Enum | Real Time, Equivalent Time | Real Time |

#### Output Parameters
None

### 28. `SetTimeDelay`
#### Description
Adjusts the horizontal delay for waveform display relative to the trigger event.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Delay | Boolean | True, False | TRUE |
| 4 | Time Delay in s | Double | - | - |

#### Output Parameters
None

### 29. `SetTimeScale`
#### Description
Configures the horizontal time scale for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timebase in s | Double | - | - |

#### Output Parameters
None

### 30. `SetTriggerCoupling`
#### Description
Defines how the oscilloscope couples the trigger source.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Coupling | Enum | DC, AC, HF Reject, LF Reject, Noise Reject | DC |

#### Output Parameters
None

### 31. `SetTriggerMode`
#### Description
Configures the trigger mode for the specified channel.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Mode | Enum | Auto, Normal | Auto |

#### Output Parameters
None

### 32. `SetInputCoupling`
#### Description
Specifies how the oscilloscope couples the input signal.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Coupling | Enum | AC, DC, Ground | DC |

#### Output Parameters
None

### 33. `SetVerticalOffset`
#### Description
Adjusts the vertical offset for the input signal.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Offset | Double | - | - |

#### Output Parameters
None

### 34. `SetVerticalPosition`
#### Description
Sets the vertical position of the input signal on the oscilloscope display.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Position | Double | - | - |

#### Output Parameters
None

### 35. `SetVerticalRange`
#### Description
Defines the vertical range for the input signal.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Range | Double | - | - |

#### Output Parameters
None

### 36. `SetVerticalScale`
#### Description
Adjusts the vertical scale for the input signal.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Scale | Double | - | - |

#### Output Parameters
None

### 37. `ToggleChannelDisplay`
#### Description
Enables or disables the display of the specified channel(s) on the oscilloscope.

**Note:** To configure for multiple Channels, enter the Channels as comma-separated inputs.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Channel? | Boolean | True, False | TRUE |

#### Output Parameters
None

### 38. `RetrieveData`
#### Description
**DEPRECATED**
This method is deprecated. Use the 'Fetch.vi' function instead for enhanced functionality.

Reason for deprecating: Added 'Initiate before Fetch?' & 'Timeout' inputs.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Waveforms | Array |

### 39. `FetchWaveform`
#### Description
Retrieves waveform data from the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Initiate before Fetch? | Boolean | True, False | TRUE |
| 4 | Timeout in ms | Double | - | 1000 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Waveforms | Array |

### 40. `GetCursorReadings`
#### Description
Reads the horizontal and vertical cursor values, along with their deltas.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | HBar Value 1 | Double |
| 2 | HBar Value 2 | Double |
| 3 | VBar Value 1 | Double |
| 4 | VBar Value 2 | Double |
| 5 | HBar Delta | Double |
| 6 | VBar Delta | Double |

### 41. `RetrieveMetadata`
#### Description
Fetches metadata such as manufacturer, model, serial number, and firmware version.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Manufacturer | String |
| 2 | Model | String |
| 3 | Serial Number | String |
| 4 | Firmware Version | String |

### 42. `GetRecordLengthInfo`
#### Description
Retrieves the horizontal record length in samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Record Length | Double |

### 43. `Init`
#### Description
Starts a new session or retrieves an existing session for the oscilloscope.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Port | Any | - | - |
| 4 | Type | String | - | - |
| 5 | Operation | Enum | Create New Session, Fetch Existing Session | Create New Session |

#### Output Parameters
None

### 44. `Initiate`
#### Description
Initiates the session for the specified Channel, preparing it to begin operations such as measurements or output delivery.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 45. `ReadMeasurement`
#### Description
Reads the result of a configured measurement parameter.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Measurement Parameter | String | - | - |
| 4 | Timeout in ms | Double | - | 1000 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Measured Value | Double |

### 46. `GetWaveformMeasurement`
#### Description
Obtains waveform measurements for the specified channel(s) based on the selected function.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Measurement Function | Enum | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Measurement Values | Array |

### 47. `GetDualChannelMeasurement`
#### Description
Fetches waveform measurements requiring two channels, such as delay or phase.

**Available Dual Channel Measurement Functions:**
- Delay
- Phase

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Measurement Function | Enum | Delay, Phase | Delay |
| 4 | Destination Channel | Integer | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Measurement Values | Array |

### 48. `RecallSetup`
#### Description
Recalls the configurations of the oscilloscope from the settings stored in the memory location or in the setup file.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | File Path | Path | - | - |
| 4 | Recall Setup | Enum | - | - |
| 5 | Memory Location | Integer | - | - |

#### Output Parameters
None

### 49. `RestoreDefaults`
#### Description
Resets the oscilloscope to its factory default settings.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 50. `SaveCurrentSetup`
#### Description
Saves the oscilloscope's current settings to a file or memory location.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Folder Path | File Path | - | - |
| 4 | File Name | String | - | Test |
| 5 | Save Setup | Enum | - | - |
| 6 | Memory Location | Integer | - | - |
| 7 | Replace Existing File? | Boolean | True, False | FALSE |

#### Output Parameters
None

