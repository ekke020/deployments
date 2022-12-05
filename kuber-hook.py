import sys 

def temp_file(file, repo, run_id, env_id):
  template = f"""apiVersion: batch/v1
kind: Job
metadata:
  generateName: kuber-workflow-approver
  annotations:
    argocd.argoproj.io/hook: PostSync
spec:
  template:
    spec:
      containers:
      - name: workflow-approver
        image: curlimages/curl
        envFrom:
        - secretRef:
            name: kuber-secret
        command: ["/bin/curl"]
        args: ["-v \
          -X POST \
          -H "Accept: application/vnd.github+json" \
          -H "Authorization: Bearer $API_TOKEN" \
          https://api.github.com/repos/ekk020/{repo}/actions/runs/{run_id}/pending_deployments \
          -d '{{\\"environment_ids\\":[{env_id}],\\"state\\":\\"approved\\",\\"comment\\":\\"Ship it!\\"}}'
        "]
      restartPolicy: Never
  backoffLimit: 2"""
  return template

def generate():
  with open('manifests/kuber-hook.yaml', 'w') as f:
    text = temp_file(f, sys.argv[1], sys.argv[2], sys.argv[3])
    f.write(text)

if __name__ == "__main__":
    generate()

          # - "curl"
          # - "-X"
          # - "POST"
          # - "-H"
          # - "Authorization: Bearer $API_TOKEN"
          # - "-H"
          # - "Content-Type: application/json"
          # - "https://api.github.com/repos/ekke020/{repo}/actions/runs/{run_id}/pending_deployments"
          # - "-d"
          # - "{{\\"environment_ids\\":[{env_id}],\\"state\\":\\"approved\\",\\"comment\\":\\"Ship it!\\"}}"