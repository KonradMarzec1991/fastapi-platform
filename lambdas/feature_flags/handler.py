"""Handlers for Lambda events"""

from feature_flags.shared import set_feature


def handler(event, context):
    """
    Expected event:
    { "action": "disable" }
    { "action": "enable" }
    """

    action = event.get("action")
    if action == "disable":
        set_feature(False)
        return {
            "status": "disabled",
            "reason": "alarm_triggered"
        }

    if action == "enable":
        set_feature(True)
        return {
            "status": "enabled",
            "reason": "alarm_recovered"
        }

    raise ValueError(f"Unknown action: {action}")
