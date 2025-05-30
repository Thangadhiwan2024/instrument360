# Spectrum Analyzer

A **Spectrum Analyzer** is an essential electronic instrument used to measure and visualize the frequency spectrum of signals. It provides insights into signal strength, noise, and distortion across a specified frequency range, making it indispensable for RF and communication system analysis.

---

## **Key Features**

### **Wide Frequency Range**
- Analyzes signals across a broad range of frequencies.
- Capable of detecting signals from a few Hz to several GHz.

### **High Resolution and Sensitivity**
- Offers fine frequency resolution to distinguish closely spaced signals.
- Detects low-level signals with high sensitivity.

### **Real-Time Spectrum Analysis**
- Continuously monitors and captures transient signals.
- Provides real-time visualization of signal behavior.

---

## **Applications**

### **RF and Wireless Communication Testing**
- Evaluates signal quality, bandwidth, and modulation accuracy.
- Identifies interference sources in wireless networks.

### **EMI/EMC Testing**
- Detects and analyzes electromagnetic interference (EMI) in electronic systems.
- Ensures compliance with electromagnetic compatibility (EMC) standards.

### **Antenna and Transmitter Characterization**
- Measures antenna radiation patterns and transmission performance.
- Verifies transmitter output power, harmonic distortion, and spurious emissions.

### **Audio and Video Signal Analysis**
- Analyzes frequency content of audio and video signals.
- Identifies noise, distortion, and unwanted signal artifacts.

---

## **Advantages**

### **Accurate Signal Visualization**
- Displays amplitude vs. frequency for detailed signal analysis.
- Identifies anomalies and unwanted frequency components.

### **Versatility and Flexibility**
- Supports a variety of input signals, including analog and digital.
- Suitable for laboratory, field, and production environments.

### **Advanced Signal Processing**
- Applies digital filtering and demodulation techniques for enhanced analysis.
- Provides actionable insights through intuitive data presentation.

---

## **Abstract Methods**
---

### 1. `AlignAll`
#### Description
This method performs a complete alignment of the instrument and returns the alignment status. It ensures optimal performance by calibrating internal components.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | alignment_status | Boolean |

### 2. `Close`
#### Description
This method is used to close the instrument session of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Operation | Enum | Close & Destroy, Destroy & Don't Close | Close & Destroy |

#### Output Parameters
None

### 3. `Get Amplitude at Selected Frequency`
#### Description
Return the amplitude of selected marker at given frequency.

**Note:** Marker type is set to position(normal).

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Active Marker | Integer | - | - |
| 4 | Frequency (Hz) | Double | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Amplitude | Double |

### 4. `Get Marker Positions`
#### Description
Retrieves the position and amplitude for a specified marker.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Marker Number | Integer | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Position | Double |
| 2 | Amplitude | Double |

### 5. `Get Sweep Points`
#### Description
Returns the configured sweep points of the spectrum analyzer.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Sweep Points | Integer |

### 6. `Get Sweep Time`
#### Description
Returns the configured sweep time of the instrument.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Sweep Time | Double |

### 7. `Init`
#### Description
This method initializes the session of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Type | String | - | - |
| 2 | Use Pre-Amp? | Boolean | true, false | - |
| 3 | Operation | Enum U16 | Create New Session | - |

#### Output Parameters
None

### 8. `LoadConfigFile`
#### Description
This method loads the instrument configuration from the selected file.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Selected Configuration | File Path | - | - |

#### Output Parameters
None

### 9. `ReadTraceData`
#### Description
This method reads trace data from the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trace Name | Enum | Trace 1, Trace 2, Trace3, Trace 4 | Trace 1 |
| 4 | Maximum Time | Double | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Initial X | Double |
| 2 | X Increment | Double |
| 3 | Y Array | 1D-Array |

### 10. `SetActiveWindow`
#### Description
This method configures the active window of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Window | Integer | - | - |

#### Output Parameters
None

### 11. `SetAmplitudeLevel`
#### Description
Configures the amplitude (vertical) settings of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Reference Level | Double | - | - |
| 4 | Reference Offset | Double | - | - |
| 5 | Units | String | - | - |
| 6 | Attenuation Level | Double | - | - |
| 7 | Auto Attenuation? | Boolean | - | - |
| 8 | Amplitude Scale | String | - | - |
| 9 | Advanced Settings | Any | - | - |

#### Output Parameters
None

### 12. `SetAveragingWithTrace`
#### Description
This method configures the averaging settings of the spectrum analyzer along with trace-specific parameters.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Average Count | I32 | - | - |
| 4 | Enable Averaging? | Boolean | true, false | - |
| 5 | Averaging Type | Any | - | - |
| 6 | Advanced Settings | Any | - | - |
| 7 | Trace Name | Enum U16 | - | - |

#### Output Parameters
None

### 13. `SetBandwidthResolution`
#### Description
This method configures the coupling and sweeping properties of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Manual Resolution BW | Double | - | - |
| 4 | Enable Auto Resolution BW? | Boolean | true, false |- |
| 5 | Enable Auto Video BW? | Boolean |true, false | - |
| 6 | Manual Video BW (Hz) | Double | - | - |
| 7 | Advanced Settings | Any | - | - |

#### Output Parameters
None

### 14. `SetDeltaMarker`
#### Description
This method configures the delta marker state of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Delta Marker Number | Integer | - | - |
| 4 | Enable? | Boolean | - | - |

#### Output Parameters
None

### 15. `SetFFTWindow`
#### Description
This method configures the FFT window type of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Windowing Type | Any | - | - |

#### Output Parameters
None

### 16. `SetInputCoupling`
#### Description
This method configures the coupling type at the analyzer RF input port.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Input Coupling | Enum | AC, DC | AC |
| 4 | Advanced Settings | Any | - | - |

#### Output Parameters
None

### 17. `SetInputImpedance`
#### Description
This method configures the input impedance of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Input Impedance (Ohm) | Enum | 50, 75 | 50 |

#### Output Parameters
None

### 18. `SetInstrumentFromMarker`
#### Description
This method makes the selected marker frequency the particular instrument setting selected. It can also make the active marker amplitude the reference level.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Instrument Setting | Enum | Reference Level, Frequency Center, Center Frequency Step, Frequency Start, Frequency Stop | Frequency Center |
| 4 | Active Marker | Integer | - | 1 |

#### Output Parameters
None

### 19. `SetMarkerPosition`
#### Description
This method configures the position of the respective marker.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Marker Position | Double | - | - |
| 4 | Marker Number | Integer | - | - |

#### Output Parameters
None

### 20. `SetMarkerState`
#### Description
This method configures the normal marker state of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Marker Number | Integer | - | - |
| 4 | Enable? | Boolean | true, false | - |

#### Output Parameters
None

### 21. `SetMode`
#### Description
This method configures the mode of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Mode | Any | - | - |

#### Output Parameters
None

### 22. `SetPreamp`
#### Description
This method configures the internal preamp state of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Preamp Settings | Enum | Disable, Enable | Disable |
| 4 | Advanced Settings | Any | - | - |

#### Output Parameters
None

### 23. `SetRFInputAttenuation`
#### Description
This method configures the RF input attenuation of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Auto ON? | Boolean | true, false | false |
| 4 | Manual Attenuator Value (dB) | Double | - | - |

#### Output Parameters
None

### 24. `SetSweepPoints`
#### Description
This method configures the sweep points of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Sweep Points | Integer | - | - |

#### Output Parameters
None

### 25. `SetSweepType`
#### Description
This method configures the sweep type of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Sweep Type | Enum | Single, Continuous, Sweep Count | Single |
| 4 | Sweep Count Value | Integer | - | - |

#### Output Parameters
None

### 26. `SetTrace`
#### Description
This method configures the type of trace to be acquired.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trace Name | Enum | Trace 1, Trace 2, Trace3, Trace 4 | Trace 1 |
| 4 | Trace Type | Enum | Clear Write, Maximum Hold, Minimum Hold, Max/Min Hold, View, Blank, Average | Clear Write |
| 5 | Advanced Settings | Any | - | - |

#### Output Parameters
None

### 27. `SetTrigger`
#### Description
This method triggers the instrument at the respective timeout value.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout (ms) | Double | - | - |

#### Output Parameters
None

### 28. `SetVerticalScale`
#### Description
This method configures the vertical scale type of the spectrum analyzer.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Vertical Scale | Enum | :Linear, Logarithmic, Linear %, Linear dB | Linear |

#### Output Parameters
None

### 29. `StopAcquisition`
#### Description
This method halts any ongoing acquisition and returns the spectrum analyzer to the Idle state. It immediately stops all measurement operations and resets the analyzer to a safe state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None
