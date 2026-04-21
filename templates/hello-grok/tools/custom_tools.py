import datetime
import os
from grok_install.tools import Tool

# Original time tool
@Tool("now")
def now() -> str:
    """Return current UTC time"""
    return datetime.datetime.now(datetime.UTC).strftime("%H:%M:%S UTC on %Y-%m-%d")

# New: Generate image using Grok's image model
@Tool("generate_image")
def generate_image(prompt: str = "A vibrant futuristic 'Hello from Grok!' poster with neon colors and X logo") -> str:
    """Generate an image using Grok Imagine and return the local image path"""
    # This calls Grok's built-in image generation (powered by Grok Imagine / Flux)
    from grok_install.image import generate
    image_path = generate(prompt, style="vivid", size="landscape")
    return image_path  # returns e.g. /tmp/grok_image_abc123.png

# New: Post to X with image attached
@Tool("post_to_x_with_image")
def post_to_x_with_image(text: str, image_path: str) -> str:
    """Post tweet with attached image to X"""
    from grok_install.x import post_tweet
    result = post_tweet(
        text=text,
        media_path=image_path,
        media_type="image/png"
    )
    return f"✅ Posted to X! Post ID: {result.get('id')}"
