#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace empty_uart_sensor {

static const uint8_t MAX_LINE_LENGTH = 8;  // Max characters for serial buffer

class EmptyUARTSensor : public sensor::Sensor, public PollingComponent, public uart::UARTDevice {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;

 protected:
  void parse_data();  // A method to parse the data read from the sensor hardware

  uint8_t buffer_data_[MAX_LINE_LENGTH];
  float parsed_value_{0.0f};  // Parsed value to be published
};

}  // namespace empty_uart_sensor
}  // namespace esphome
