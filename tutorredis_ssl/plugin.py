from tutor import hooks

@hooks.Filters.CONFIG_DEFAULTS.add()
def _add_redis_transport_default(items):
    items.append(("REDIS_TRANSPORT", "redis"))
    return items