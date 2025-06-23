from esphome import automation
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    CONF_ON_STATE,
    CONF_STATE,
    CONF_TRIGGER_ID,
)

empty_automation_ns = cg.esphome_ns.namespace("empty_automation")
EmptyAutomation = empty_automation_ns.class_("EmptyAutomation", cg.Component)
# Actions
EmptyAutomationSetStateAction = empty_automation_ns.class_(
    "EmptyAutomationSetStateAction", automation.Action
)
# Conditions
EmptyAutomationCondition = empty_automation_ns.class_(
    "EmptyAutomationCondition", automation.Condition
)
# Triggers
StateTrigger = empty_automation_ns.class_(
    "StateTrigger", automation.Trigger.template(bool)
)


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(EmptyAutomation),
        cv.Optional(CONF_ON_STATE): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(StateTrigger),
            }
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


EMPTY_AUTOMATION_ACTION_SCHEMA = cv.maybe_simple_value(
    {
        cv.Required(CONF_ID): cv.use_id(EmptyAutomation),
        cv.Required(CONF_STATE): cv.boolean,
    },
    key=CONF_STATE,
)


EMPTY_AUTOMATION_CONDITION_SCHEMA = automation.maybe_simple_id(
    {
        cv.Required(CONF_ID): cv.use_id(EmptyAutomation),
    }
)


@automation.register_action(
    "empty_automation.set_state",
    EmptyAutomationSetStateAction,
    EMPTY_AUTOMATION_ACTION_SCHEMA,
)
async def empty_automation_set_state_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    cg.add(var.set_state(config[CONF_STATE]))
    return var


@automation.register_condition(
    "empty_automation.component_on",
    EmptyAutomationCondition,
    EMPTY_AUTOMATION_CONDITION_SCHEMA,
)
async def empty_automation_component_on_to_code(
    config, condition_id, template_arg, args
):
    paren = await cg.get_variable(config[CONF_ID])
    return cg.new_Pvariable(condition_id, template_arg, paren, True)


@automation.register_condition(
    "empty_automation.component_off",
    EmptyAutomationCondition,
    EMPTY_AUTOMATION_CONDITION_SCHEMA,
)
async def empty_automation_component_off_to_code(
    config, condition_id, template_arg, args
):
    paren = await cg.get_variable(config[CONF_ID])
    return cg.new_Pvariable(condition_id, template_arg, paren, False)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    for conf in config.get(CONF_ON_STATE, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [(bool, "x")], conf)
