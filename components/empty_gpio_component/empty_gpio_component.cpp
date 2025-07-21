#include "esphome/core/log.h"
#include "empty_gpio_component.h"

namespace esphome {
namespace empty_gpio_component {

static const char *TAG = "empty_gpio_component.component";

void EmptyGPIOComponent::setup() {
  ESP_LOGCONFIG(TAG, "Running setup");
  this->pin_->setup();
  this->pin_->digital_write(true);
}

void EmptyGPIOComponent::loop() {

}

void EmptyGPIOComponent::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty GPIO component");
    LOG_PIN("  Pin: ", this->pin_);
}


}  // namespace empty_gpio_component
}  // namespace esphome