<a href="https://esphome.io/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./logo-text-on-dark.svg", alt="ESPHome Logo">
    <img src="./logo-text-on-light.svg" alt="ESPHome Logo">
  </picture>
</a>

# ESPHome starter components

This repository contains a number of examples in the form of empty components which can be used as templates to quickly
develop your own ([external](https://esphome.io/components/external_components)) components for
[ESPHome](https://esphome.io).

## How to use the examples in this repository

All examples are in the [`components`](components/) directory of this repository. The
[`test_empty_components.yaml`](test_empty_components.yaml) file contains configuration examples for the various
components.

The easiest way to develop components/platforms for use within ESPHome is to use
[external components](https://esphome.io/components/external_components). To use a particular component from this
repository for your project:

1. Create an `external_components` directory in your ESPHome configuration directory (the directory where your `.yaml` 
  files are located).
1. Copy the directory (and all of its contents!) of an empty component into your `external_components` directory. You
  should end up with something like this: `external_components/empty_sensor/`
1. Find the configuration entry for the empty component in [`test_empty_components.yaml`](test_empty_components.yaml) 
   and copy it into your own `.yaml` file.
1. Compile with `esphome compile your_config.yaml` where `your_config.yaml` is your own `.yaml` file.
1. No errors? Great! You can now start modifying the empty component to turn it into your own (external) component.

## Going further

- [Developer documentation](https://developers.esphome.io)
- [Component architecture overview](https://developers.esphome.io/architecture/components/)
