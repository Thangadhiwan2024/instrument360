# Source Measure Unit (SMU)

A **Source Measure Unit (SMU)** is a highly accurate instrument that combines **sourcing** and **measuring** capabilities into one device. It is widely used for testing semiconductors, characterizing components, and analyzing materials.

---

## **Key Features**

### **Precision Sourcing**
- Provides accurate voltage or current to the **Device Under Test (DUT)**.
- Ensures stability and minimal noise during sourcing.

### **Four-Quadrant Operation**
- **Quadrant I:** Sourcing voltage and sourcing current.
- **Quadrant II:** Sourcing voltage and sinking current.
- **Quadrant III:** Sinking voltage and sinking current.
- **Quadrant IV:** Sinking voltage and sourcing current.

---

## **Applications**
### **Semiconductor Testing**
- Evaluates I-V characteristics of transistors, diodes, and other semiconductor devices.
- Measures leakage current and threshold voltage with high precision.

### **Component Characterization**
- Analyzes passive and active components, such as resistors, capacitors, and inductors.
- Validates component performance under various operating conditions.

### **Material Analysis**
- Assesses electrical properties of materials by measuring resistivity and conductivity.
- Conducts leakage and breakdown voltage tests.

---

## **Advantages**
### **High Accuracy and Stability**
- Ensures precise control over source and measurement parameters.
- Minimizes errors and noise for sensitive applications.

### **Simplified Test Setup**
- Combines source and measurement functions into one instrument.
- Reduces complexity and improves test efficiency.

### **Automation and Integration**
- Supports integration with automated test systems.
- Enables consistent and efficient test execution.

---

## **Abstract Methods**
---

### 1. `Abort`
#### Description
Terminates the session for the SMU by halting any ongoing operations and resetting the session to a safe state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
None

### 2. `Close`
#### Description
Ends the session for the SMU by releasing the communication channel and freeing resources.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
None

### 3. `ConnectDisconnectOutput`
#### Description
Connects or disconnects the output of the specified SMU channel.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | state | enum | Connect, Disconnect | Disconnect |

#### Output Parameters
None

### 4. `SetOverCurrentProtection`
#### Description
Configures over-current protection (OCP) for the specified channel by enabling or disabling protection and setting the maximum allowable current limit.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | enable_ocp | bool | True, False | True |
| 4 | over_current_protection | float | - | 0.1A |

#### Output Parameters
None

### 5. `SetOverVoltageProtection`
#### Description
Configures over-voltage protection (OVP) for the specified channel by enabling or disabling protection and setting the maximum allowable voltage limit.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | enable_ovp | bool | True, False | True |
| 4 | over_voltage_protection | float | - | 10V |

#### Output Parameters
None

### 6. `SetPulseSourceMode`
#### Description
Configures the pulse source mode for the specified channel to control how pulses are generated.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_mode | enum | Pulse Voltage, Pulse Current | Pulse Voltage |

#### Output Parameters
None

### 7. `SetPulseTimings`
#### Description
Configures the pulse period and pulse width for the specified channel to define the timing of pulse generation.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_period | float | - | 50ms |
| 4 | pulse_width | float | - | 25ms |

#### Output Parameters
None

### 8. `SetSenseMode`
#### Description
Configures the sense mode for the specified channel to measure voltage or current either at the source (local) or at the load (remote).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | sense | enum | Local, Remote | Local |

#### Output Parameters
None

### 9. `SetSourceMode`
#### Description
Configures the source mode for the specified channel to either control voltage or current.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | dc_source_mode | enum | Voltage, Current | Voltage |

#### Output Parameters
None

### 10. `SetSourceDelay`
#### Description
Sets the source delay time for the specified channel to introduce a delay before enabling the output.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | enable_source_delay | bool | True, False | False |
| 4 | source_delay | float | - | 0.1 |

#### Output Parameters
None

### 11. `ToggleOutputState`
#### Description
Enables or disables the output for the specified channel to control power delivery.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | state | bool | True, False | True |

#### Output Parameters
None

### 12. `Init`
#### Description
Initializes the session for the SMU by establishing communication and preparing the device for further commands.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
None

### 13. `Initiate`
#### Description
Initiates the session for the specified channel, preparing it to begin operations such as measurements or output delivery.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
None

### 14. `GetCurrentMeasurement`
#### Description
Measures and returns the current for the specified channel. This function retrieves the instantaneous current flowing through the circuit or device connected to the SMU (Source Measure Unit).

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | current | array |

### 15. `GetVoltageMeasurement`
#### Description
Measures and returns the voltage for the specified channel. This function captures the voltage across the connected circuit or device with high precision.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | voltage | array |

### 16. `Reset`
#### Description
Resets the instrument settings to the factory or default state. It terminates any ongoing operations and restores the initial configurations, ensuring a clean state before performing subsequent tasks.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |

#### Output Parameters
None

### 17. `SetCurrentParameters`
#### Description
Configures the current level and voltage limit for the specified channel. It defines the target current and associated safety limits to protect the circuit while sourcing current.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | current_level | float | - | 0.1A |
| 4 | voltage_limit | float | - | 2V |
| 5 | current_level_range | float | - | 0.1A |
| 6 | voltage_limit_range | float | - | 6V |
| 7 | source_delay | float | - | 0.1 |

#### Output Parameters
None

### 18. `SetCurrentLimit`
#### Description
Sets the maximum allowable current for the specified channel. This function establishes a protection limit, preventing the channel from sourcing excessive current that could damage the connected device.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | current_limit | float | - | 0.1A |

#### Output Parameters
None

### 19. `SetCurrentLimitRange`
#### Description
Defines the permissible range for the current limit and optionally enables auto-ranging for dynamic range adjustment based on load requirements.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | current_limit_range | float | - | 0.1A |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 20. `SetCurrentLevel`
#### Description
Configures the desired current level for the specified channel. This function precisely sets the current that the channel will source to the connected device.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | current_level | float | - | 0.1A |

#### Output Parameters
None

### 21. `SetCurrentRange`
#### Description
Sets the permissible range for the current level and optionally enables auto-ranging to adjust the range dynamically.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | current_level_range | float | - | 0.1A |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 22. `SetVoltageLimit`
#### Description
Sets the maximum allowable voltage for the specified channel, ensuring that the applied voltage does not exceed a safe threshold.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | voltage_limit | float | - | 2V |

#### Output Parameters
None

### 23. `SetVoltageLimitRange`
#### Description
Defines the permissible range for the voltage limit and enables auto-ranging for automatic adjustment of the range.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | voltage_limit_range | float | - | 6V |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 24. `SetVoltageLevel`
#### Description
Configures the desired voltage level for the specified channel. This function ensures accurate voltage sourcing to the connected circuit.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | voltage_level | float | - | 2V |

#### Output Parameters
None

### 25. `SetVoltageRange`
#### Description
Sets the voltage range with optional auto-ranging to dynamically adjust the range depending on load requirements.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | voltage_level_range | float | - | 6V |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 26. `SetPulseBaseCurrentLimit`
#### Description
Configures the limit for the pulse base current to ensure safe operation during pulse generation.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_limit | float | - | 10mA |

#### Output Parameters
None

### 27. `SetPulseBaseCurrentLevel`
#### Description
Sets the desired pulse base current level for the specified channel, ensuring that pulse operations are performed with the correct parameters.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_level | float | - | 0.1A |

#### Output Parameters
None

### 28. `SetPulseBaseVoltageLimit`
#### Description
Configures the maximum allowable voltage limit for the pulse base operation, preventing excessive voltage from being applied.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_limit | float | - | 0.1V |

#### Output Parameters
None

### 29. `SetPulseBaseVoltageLevel`
#### Description
Sets the desired pulse base voltage level for the specified channel, ensuring that the pulse voltage meets operational requirements.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_level | float | - | 0.2V |

#### Output Parameters
None

### 30. `SetPulseCurrentLimit`
#### Description
Sets the pulse current limit for the specified channel to ensure the current does not exceed the defined threshold during pulse operations. This protects the device under test (DUT) from excessive current that could cause damage.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_limit | float | - | 0.1A |

#### Output Parameters
None

### 31. `SetPulseCurrentLimitRange`
#### Description
Sets the pulse current limit range for the specified channel, allowing flexibility in defining the allowable range for pulse current limits. When auto-range is enabled, the system dynamically adjusts the range for optimal performance.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_limit_range | float | - | 0.1A |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 32. `SetPulseCurrentLevel`
#### Description
Sets the pulse current level for the specified channel, determining the desired magnitude of pulse current that should be applied to the DUT during operations.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_level | float | - | 0.1A |

#### Output Parameters
None

### 33. `SetPulseCurrentLevelRange`
#### Description
Sets the pulse current level range for the specified channel to define the allowable range within which the pulse current level can be set. When auto-range is enabled, the system adjusts the range based on varying conditions.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_current_level_range | float | - | - |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 34. `SetPulseVoltageLimit`
#### Description
Sets the pulse voltage limit for the specified channel, ensuring that the voltage applied during pulse operations does not exceed the defined threshold, protecting the DUT from excessive voltage.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_limit | float | - | 3V |

#### Output Parameters
None

### 35. `SetPulseVoltageLimitRange`
#### Description
Sets the pulse voltage limit range for the specified channel, allowing the definition of a permissible range for pulse voltage limits. When auto-range is enabled, the system dynamically adapts the range for optimal voltage control.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_limit_range | float | - | 3V |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None

### 36. `SetPulseVoltageLevel`
#### Description
Sets the pulse voltage level for the specified channel, specifying the desired voltage to be applied during pulse operations. This value determines the voltage intensity delivered to the DUT.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_level | float | - | 1V |

#### Output Parameters
None

### 37. `SetPulseVoltageLevelRange`
#### Description
Sets the pulse voltage level range for the specified channel, defining the acceptable range within which the pulse voltage level can be set. When auto-range is enabled, the system dynamically adjusts the range based on varying conditions.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | channel | String | - | - |
| 3 | pulse_voltage_level_range | float | - | 3V |
| 4 | auto_range | bool | True, False | False |

#### Output Parameters
None