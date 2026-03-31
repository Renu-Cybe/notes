#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI image generation via Volcengine (Doubao) API.
"""
import argparse
import base64
import json
import requests
import os
import sys


def generate_image(prompt: str, api_key: str, model: str = "doubao-seedream-5-0-260128",
                   base_url: str = "https://ark.cn-beijing.volces.com/api/v3",
                   output_path: str = "output/cover.png") -> dict:
    """
    Generate image via Volcengine Doubao API.

    Args:
        prompt: Image generation prompt
        api_key: Volcengine API key
        model: Model ID
        base_url: API base URL
        output_path: Output file path

    Returns:
        dict with 'ok', 'path', 'error' fields
    """
    try:
        url = f"{base_url}/images/generations"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model,
            "prompt": prompt,
            "size": "1024x1024",
            "response_format": "url"
        }

        resp = requests.post(url, headers=headers, json=data, timeout=60)
        result = resp.json()

        if "data" in result and len(result["data"]) > 0:
            image_url = result["data"][0].get("url", "")
            if image_url:
                # Download image
                img_resp = requests.get(image_url, timeout=30)
                if img_resp.status_code == 200:
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(img_resp.content)
                    return {"ok": True, "path": output_path}
                else:
                    return {"ok": False, "error": f"Download failed: {img_resp.status_code}"}
            else:
                return {"ok": False, "error": "No image URL in response"}
        else:
            return {"ok": False, "error": result.get("error", result)}

    except Exception as e:
        return {"ok": False, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Generate image via Volcengine API")
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--output", default="output/cover.png", help="Output file path")
    parser.add_argument("--config", default="config.yaml", help="Config file path")
    args = parser.parse_args()

    # Load config
    import yaml
    config_path = os.path.join(os.path.dirname(__file__), '..', args.config)
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        api_key = config.get('image', {}).get('api_key', '')
        model = config.get('image', {}).get('model', 'doubao-seedream-5-0-260128')
        base_url = config.get('image', {}).get('base_url', 'https://ark.cn-beijing.volces.com/api/v3')
    else:
        print(f"Config file not found: {config_path}")
        sys.exit(1)

    result = generate_image(args.prompt, api_key, model, base_url, args.output)

    if result['ok']:
        print(f"Image saved to: {result['path']}")
    else:
        print(f"Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()