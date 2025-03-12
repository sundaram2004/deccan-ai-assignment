import sentry_sdk

from core.config import settings


def setup_sentry():
    sentry_sdk.init(
        settings.SENTRY_DSN,
        traces_sample_rate=1.0,
    )
