#pragma once

#include "esphome/core/component.h"
#include "esphome/components/output/binary_output.h"
#include "esphome/components/fan/fan.h"

namespace esphome {
namespace empty_fan {

class EmptyFan : public fan::Fan, public Component {
 public:
  void set_direction(output::BinaryOutput *output) { this->direction_output_ = output; }
  void set_oscillating(output::BinaryOutput *output) { this->oscillating_output_ = output; }
  void set_output(output::BinaryOutput *output) { this->output_ = output; }
  fan::FanTraits get_traits() override { return this->traits_; }
  void setup() override;
  void dump_config() override;

 protected:
  void control(const fan::FanCall &call) override;
  void write_state_();

  fan::FanTraits traits_;
  output::BinaryOutput *direction_output_;
  output::BinaryOutput *oscillating_output_;
  output::BinaryOutput *output_;
};

}  // namespace empty_fan
}  // namespace esphome
