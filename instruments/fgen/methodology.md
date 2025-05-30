# Function Generator (FGEN)

A **Function Generator (FGEN)** is an electronic device that generates various waveforms, such as **sine**, **square**, and **triangle** signals, used for testing, troubleshooting, and designing electronic circuits.

---

## **Key Features**

### **Multiple Waveform Generation**
- Produces sine, square, triangle, ramp, and pulse waveforms.
- Provides flexibility in simulating different signal types.

### **Adjustable Frequency and Amplitude**
- Allows precise control over output frequency and voltage levels.
- Supports a wide range of frequency settings to meet diverse application needs.

### **Modulation Capability**
- Supports amplitude modulation (AM), frequency modulation (FM), and phase modulation (PM).
- Enables advanced signal testing and simulation.

---

## **Applications**

### **Circuit Testing and Debugging**
- Simulates input signals to test circuit responses.
- Helps diagnose and troubleshoot signal processing issues.

### **Device Characterization**
- Evaluates the performance of amplifiers, filters, and other components.
- Assesses frequency response, gain, and distortion characteristics.

### **Educational and Research Purposes**
- Demonstrates signal behavior in laboratories and classrooms.
- Provides hands-on learning for waveform analysis and circuit design.

---

## **Advantages**

### **Versatility and Flexibility**
- Generates multiple waveforms for diverse applications.
- Adjustable parameters allow customized signal generation.

### **High Signal Fidelity**
- Produces accurate and stable waveforms with minimal distortion.
- Ensures reliable performance in sensitive applications.

### **Ease of Integration**
- Interfaces with oscilloscope, spectrum analyzers, and other test equipment.
- Facilitates automated testing and system analysis.

---

## **Abstract Methods**
---

### 1. `Abort`
#### Description
Stops the current operation on the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 2. `Close`
#### Description
Terminates the instrument session for the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Operation | Enum | Close & Destroy, Destroy & Don't Close| Close & Destroy |

#### Output Parameters
None

### 3. `Configure Burst Mode`
#### Description
Sets up burst modulation for the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Enable Burst Mode | Boolean | false, true | false |
| 4 | Burst Phase | Double | - | - |
| 5 | Burst Cycle | Integer | - | 1 |
| 6 | Burst Period | Double | - | - |
| 7 | Trigger Source | Enum |Internal, External, Manual | Internal |
| 8 | Additional input | Any | - | - |
| 9 | Burst Mode | Enum | Triggered, Gated | Triggered |
| 10 | Gate Polarity | Enum | Normal, Inverted | Normal |

#### Output Parameters
None

### 4. `Set High Low Level`
#### Description
Configures the high-level and low-level of the output signal for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Value High in V | Double | - | 0.5 |
| 4 | Value Low in V | Double | -0.5 |

#### Output Parameters
None

### 5. `Set Output Polarity`
#### Description
Inverts the waveform relative to the offset voltage for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Output Polarity | Enum | Normal, Inverted | Normal |

#### Output Parameters
None

### 6. `Set Pulse Delay`
#### Description
Configures the pulse delay value and unit for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Pulse Delay Unit | Enum | Seconds, Radians, Percent, Degree | Seconds |
| 4 | Pulse Delay Value | Double | - | - |

#### Output Parameters
None

### 7. `Set Pulse Duty Cycle`
#### Description
Configures the Duty Cycle of the Pulse waveform for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Duty Cycle | Double| - | 50.00 |

#### Output Parameters
None

### 8. `Configure Pulse Waveform`
#### Description
Sets up the parameters for the pulse waveform for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Leading Edge Time | Double | - | 5E-9 |
| 4 | Trailing Edge Time | Double | - | 5E-9 |
| 5 | Pulse Width | Double | - | 0.0001 |
| 6 | Pulse Period | Double | - | 0.001 |

#### Output Parameters
None

### 9. `Set Ramp Waveform`
#### Description
Configures the Symmetry of the Ramp waveform for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Percentage | Double | - | 100.0 |

#### Output Parameters
None

### 10. `Set Square Waveform`
#### Description
Configures the Duty Cycle of the Square waveform for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Duty Cycle | Double | - | 50.00 |

#### Output Parameters
None

### 11. `Set Standard Waveform`
#### Description
Configures the waveform shape for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Dc Offset | Double | - | - |
| 4 | Frequency | Double | - | 1000 |
| 5 | Start Phase | Double | -| - |
| 6 | Waveform | Enum| Sine, Square, Ramp Up, DC, Noise, Triangle, Pulse, Ramp Down, Ramp | Sine |
| 7 | Amplitude | Double | - | 0.10 |
| 8 | Additional input | Any | - | - |

#### Output Parameters
None

### 12. `Configure Frequency Sweep`
#### Description
Sets up the Frequency Sweep for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Power Array | 1D-Array | - | - |
| 4 | Dwell Time Array | 1D-Array | - | 0.002 |
| 5 | Frequency Array | 1D-Array | - | 1000 |

#### Output Parameters
None

### 13. `Configure Channel Tracking`
#### Description
Sets up tracking mode for channels 1 and 2 of a two-channel waveform generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Track Mode | Enum | ON, OFF, Invert | ON |
| 4 | Source Channel | Enum | 1, 2 | 1 |

#### Output Parameters
None

### 14. `Set Trigger Slope`
#### Description
Configures the polarity of the External Trigger terminal for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Slope | Enum | Positive, Negative | Positive |

#### Output Parameters
None

### 15. `Set Trigger Source`
#### Description
Configures the Trigger Source for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Source | Enum  | Immediate, External, Software(Bus), Internal | Software(Bus) |

#### Output Parameters
None

### 16. `Disable Channel Output`
#### Description
Turns off the output of the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 17. `Enable Channel Output`
#### Description
Turns on the output of the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 18. `Init`
#### Description
Starts the session of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | FGEN Type | String | - | - |
| 4 | Operation | Enum | Close & Destroy, Destroy & Don't Close| Close & Destroy |

#### Output Parameters
None

### 19. `Initiate`
#### Description
Begins the specified channel(s) of the Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 20. `Reset`
#### Description
Resets the specified Function Generator.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 21. `Send Software Trigger`
#### Description
Sends a software trigger to the specified Function Generator. Trigger Source must be set to 'Software(Bus)' to send a software trigger.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 22. `Set Load Impedance`
#### Description
Configures the load impedance for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Load Impedance | Double | - | 50.0 |

#### Output Parameters
None

### 23. `Set Output Impedance`
#### Description
Configures the output impedance for the specified channel(s).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Impedance | Double | - | 50.0 |

#### Output Parameters
None




