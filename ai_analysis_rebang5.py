"""API key configuration for ai_analysis_rebang5.

将 API Key 直接写在代码中，避免青龙环境变量读取失败。
请把下面两个占位符替换成你自己的真实值。
"""

# TODO: 替换为你自己的真实值
BAILIAN_API_KEY = "YOUR_BAILIAN_API_KEY"
V3_API_KEY = "YOUR_V3_API_KEY"


def get_api_keys() -> tuple[str, str]:
    """Return configured API keys."""
    return BAILIAN_API_KEY, V3_API_KEY
