# Electronic Load

An **Electronic Load** is a programmable instrument used to simulate various electrical loads by dissipating power from a **Device Under Test (DUT)**. It is commonly used in semiconductor validation, power supply testing, and battery performance evaluation.

---

## **Key Features**

### **Constant Operating Modes**
- **Constant Current (CC):** Maintains a fixed current regardless of voltage changes.
- **Constant Voltage (CV):** Holds a steady voltage while varying current.
- **Constant Power (CP):** Regulates power consumption by adjusting current and voltage.
- **Constant Resistance (CR):** Simulates a fixed resistive load for testing.

### **Dynamic Load Simulation**
- Supports fast load changes to simulate real-world operating conditions.
- Allows accurate evaluation of transient response and stability.

### **Parallel and Series Operation**
- Enables connection of multiple loads to handle high-power applications.
- Supports both parallel and series configurations for greater flexibility.

---

## **Applications**

### **Power Supply Testing**
- Verifies the performance and stability of power supplies under different load conditions.
- Evaluates output voltage regulation, efficiency, and ripple response.

### **Battery and Fuel Cell Testing**
- Simulates discharge profiles to assess battery capacity and lifecycle.
- Measures internal resistance and validates the efficiency of energy storage systems.

### **Semiconductor Validation**
- Tests voltage and current limits of semiconductor devices.
- Evaluates thermal performance and safe operating areas (SOA).

### **DC-DC Converter Analysis**
- Assesses the dynamic response and efficiency of DC-DC converters.
- Simulates load changes to evaluate switching performance.

---

## **Advantages**

### **High Accuracy and Resolution**
- Provides precise control over load conditions.
- Ensures reliable results for sensitive applications.

### **Versatile and Configurable**
- Supports multiple operating modes to suit a variety of test scenarios.
- Offers programmable sequences to automate testing processes.

### **Protection and Safety Features**
- Includes overvoltage, overcurrent, and overpower protection.
- Prevents damage to both the DUT and the electronic load.

---

## **Abstract Methods**
---

### 1. `Abort`
#### Description
Stops any ongoing operations on the Electronic Load, bringing it to a safe state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 2. `Close`
#### Description
Terminates the instrument session of the Electronic Load, releasing all allocated resources.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 3. `SetAutoRange`
#### Description
Sets auto range settings for the selected type in specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | range_type | Enum | Current, Voltage, Power, Conductance | Current |
| 4 | auto_range | Boolean | true, false | false |

#### Output Parameters
None

### 4. `SetManualRange`
#### Description
Sets the manual range for the selected type in specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | range_type | Enum | Current, Voltage, Power, Conductance | Current |
| 4 | manual_range | Double | - | - |

#### Output Parameters
None

### 5. `SetOperationMode`
#### Description
Sets the operation mode of the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | operation_mode | Enum | Constant Current(CC), Constant Voltage(CV),  Constant Power (CP), Constant Resistance (CR) | Constant Current (CC) |

#### Output Parameters
None

### 6. `SetOverCurrentProtection`
#### Description
Sets Over Current Protection (OCP) limit and mode for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | ocp_limit | Double | - | 33 A |
| 4 | ocp_mode | Enum | Limit, Trip | Limit |

#### Output Parameters
None

### 7. `SetOverPowerProtection`
#### Description
Sets Over Power Protection (OPP) limit and mode for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | opp_limit | Double | - | 165 W |
| 4 | opp_mode | Enum | Limit, Trip | Limit |

#### Output Parameters
None

### 8. `SetRange`
#### Description
Sets the range for the selected type in specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | range | Enum | Low, Medium, High | Low |
| 4 | range_type | Enum | Current, Voltage, Power, Conductance | Current |

#### Output Parameters
None

### 9. `SetResponseSpeed`
#### Description
Sets the response speed for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | response_speed | Enum | Normal Response Speed, 1/2 the Normal Response Speed, 1/5 Normal Response Speed, 1/10 Normal Response Speed, Fast Response Speed | Normal Response Speed |

#### Output Parameters
None

### 10. `SetSlewRate`
#### Description
Sets the current slew rate in amps per microseconds for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | slew_rate | Double | - | 2.4 A/µs |

#### Output Parameters
None

### 11. `SetSoftStartDuration`
#### Description
Sets the Soft Start Duration (applicable only for Constant Current Mode) for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | soft_start_duration | Double | - | - |

#### Output Parameters
None

### 12. `SetSwitchingFunction`
#### Description
Sets the switching properties for the specified channel(s) of the Electronic Load. Switching properties are used to execute two load settings repetitively. This is applicable only for CC and CR Modes.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | enable_switching | Boolean | true, false | false |
| 4 | duty_cycle | Double | - | 5% |
| 5 | pulse_frequency | Double | - | 1 Hz |
| 6 | switching_level | Double | - | - |

#### Output Parameters
None

### 13. `SetTiming`
#### Description
Sets the Cutoff Time for the specified channel(s) of the Electronic Load. Cutoff Time is the auto load off time which turns off the load after the specified time elapses.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | cutoff_time | I32 | - | - |

#### Output Parameters
None

### 14. `SetUnderVoltageProtection`
#### Description
Turns ON/OFF Under Voltage Protection (UVP) and sets its limit for the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | uvp_limit | Double | - | - |
| 4 | enable_uvp | Boolean | true, false | false |

#### Output Parameters
None

### 15. `SetValue`
#### Description
Sets the value for the selected type in specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | value | Double | - | - |
| 4 | value_type | Enum | Current, Voltage, Power, Conductance | Current |

#### Output Parameters
None

### 16. `ToggleLoad`
#### Description
Enables/disables load from the specified channel(s) of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | enable_load | Boolean | true, false | false |

#### Output Parameters
None

### 17. `Init`
#### Description
Initializes the session of the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 18. `MeasureValues`
#### Description
Measures the current, voltage, power, and elapsed time values from the specified channel.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | current | Double |
| 2 | voltage | Double |
| 3 | power | Double |
| 4 | elapsed_time | Double |

### 19. `Reset`
#### Description
Resets the Electronic Load.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:----:|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None


