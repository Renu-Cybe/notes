#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article to WeChat draft box with proper encoding."""
import requests
import json
import re

# Read access token
with open('output/.access_token', 'r') as f:
    access_token = f.read().strip()

# Read cover media_id
with open('output/.cover_media_id', 'r') as f:
    thumb_media_id = f.read().strip()

# Read article
with open('output/2026-03-31-claude-code-tutorial.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse content
lines = content.split('\n')
body = '\n'.join(lines[1:])

# Title (shorter for WeChat)
title = '30分钟用AI写出你的第一个工具'

# Remove edit anchors and tags
body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
body = re.sub(r'\*\*标签\*\*.*', '', body, flags=re.DOTALL)

# Convert to HTML
html = body
html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
html = re.sub(r'```bash\n(.*?)\n```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
html = re.sub(r'\n\n', r'</p><p>', html)
html = '<p>' + html + '</p>'

# Clean up
html = html.replace('<p></p>', '')
html = html.replace('<p><h2>', '<h2>')
html = html.replace('</h2></p>', '</h2>')
html = html.replace('<p><h3>', '<h3>')
html = html.replace('</h3></p>', '</h3>')
html = html.replace('<p><pre>', '<pre>')
html = html.replace('</pre></p>', '</pre>')
html = html.replace('<p><blockquote>', '<blockquote>')
html = html.replace('</blockquote></p>', '</blockquote>')

# Summary
summary = '想用AI但不知道从哪开始？教你用Claude Code，30分钟写出第一个小助手。零基础友好，有手就行。'

print('Title:', title)
print('Summary:', summary[:30], '...')
print('Content length:', len(html), 'chars')

# Create draft - use requests with properly encoded JSON
url = f'https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}'

payload = {
    'articles': [{
        'title': title,
        'author': 'AI平权者',
        'digest': summary,
        'content': html,
        'thumb_media_id': thumb_media_id,
        'need_open_comment': 0,
        'only_fans_can_comment': 0
    }]
}

# Send as raw JSON string with UTF-8 encoding
json_str = json.dumps(payload, ensure_ascii=False)
resp = requests.post(url, data=json_str.encode('utf-8'), headers={'Content-Type': 'application/json; charset=utf-8'}, timeout=30)
result = resp.json()

if 'media_id' in result:
    print('SUCCESS!')
    print('media_id:', result['media_id'])
    with open('output/.draft_media_id', 'w') as f:
        f.write(result['media_id'])
else:
    print('ERROR:', result)