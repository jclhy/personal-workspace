import subprocess, json, urllib.request

# 获取 token
result = subprocess.run(
    ['lark-cli', 'api', 'GET', '/open-apis/auth/v3/tenant_access_token/internal',
     '--data', '{"app_id":"cli_a97f48c2b0b85cd2"}'],
    capture_output=True, text=True,
    env={"PATH": "/usr/bin", "LARK_CLI_NO_PROXY": "1"}
)

output = result.stderr + result.stdout
token = ""
for line in output.split('\n'):
    if '"tenant_access_token"' in line:
        try:
            token = json.loads(line).get('tenant_access_token', '')
            break
        except:
            pass

if not token:
    print("Failed to get token")
    exit(1)

print(f"Got token: {token[:20]}...")

# 更新记录
url = "https://open.feishu.cn/open-apis/bitable/v1/apps/YXZObpKA4a7ir2snyxjc618LnAe/tables/tblxHmwmCQzBnegk/records/recvlbR9fXKnZZ"
data = json.dumps({"fields": {"状态": {"name": "已完成"}}}).encode()
req = urllib.request.Request(url, data=data, method='PUT')
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')

try:
    resp = urllib.request.urlopen(req)
    print(resp.read().decode())
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
