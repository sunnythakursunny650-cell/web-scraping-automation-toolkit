from pydantic import BaseModel, field_validator
import re

class BookRecord(BaseModel):
    title: str
    price_gbp: float
    rating: int
    availability: str
    url: str

    @field_validator("price_gbp", mode="before")
    def clean_price(cls, val):
        if isinstance(val, str):
            clean_val = re.sub(r"[^\d.]", "", val)
            return float(clean_val)
        return float(val)

    @field_validator("rating", mode="before")
    def validate_rating(cls, val):
        rating_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        if isinstance(val, str):
            val_lower = val.lower()
            if val_lower in rating_map:
                return rating_map[val_lower]
        val_int = int(val)
        if 1 <= val_int <= 5:
            return val_int
        raise ValueError("Rating must be between 1 and 5")