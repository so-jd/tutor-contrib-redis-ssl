from tutor import hooks

hooks.Filters.CONFIG_DEFAULTS.add_item(
    [
        ("REDIS_TRANSPORT", "redis"),
    ]
)