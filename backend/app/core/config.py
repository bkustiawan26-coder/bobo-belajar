from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="BOBO_", extra="ignore")

    env: str = "development"
    database_url: str = "postgresql+psycopg://bobo:bobo@localhost:5432/bobo"
    jwt_secret: str = Field(min_length=32)
    jwt_issuer: str = "bobo-belajar"
    access_ttl_minutes: int = 30
    student_ttl_days: int = 30
    refresh_ttl_days: int = 60
    cors_origins: str = "http://localhost:3000"
    pin_max_attempts: int = 5
    pin_lock_minutes: int = 15
    login_rate_per_minute: int = 10
    assessment_grace_seconds: int = 30

    ai_provider: str = "grounded"
    ai_model: str = "grounded-v1"
    ai_timeout_seconds: float = 20.0
    ai_global_daily_cost_limit_usd: float = 5.0
    ai_max_output_tokens: int = 400
    anthropic_api_key: str | None = None
    anthropic_base_url: str = "https://api.anthropic.com"
    openai_compat_base_url: str | None = None
    openai_compat_api_key: str | None = None
    ai_price_input_per_mtok: float = 0.0
    ai_price_output_per_mtok: float = 0.0

    free_tutor_daily_limit: int = 10
    premium_tutor_daily_limit: int = 40
    free_parent_assistant_daily_limit: int = 10
    premium_parent_assistant_daily_limit: int = 40

    privacy_policy_version: str = "2026-11"

    @field_validator("jwt_secret")
    @classmethod
    def no_placeholder(cls, v: str) -> str:
        if v.lower().startswith("change") or v.lower().startswith("replace"):
            raise ValueError("BOBO_JWT_SECRET must be set to a random value")
        return v

    @property
    def cors_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
