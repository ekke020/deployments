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
        command:
          - "curl"
          - "-X"
          - "POST"
          - "-H"
          - "Authorization: Bearer \\"$API_TOKEN\\""
          - "-H"
          - "Content-Type: application/json"
          - "https://api.github.com/repos/PricerAB/{repo}/actions/runs/{run_id}/pending_deployments"
          - "-d"
          - "{{\\"environment_ids\\":[{env_id}],\\"state\\":\\"approved\\",\\"comment\\":\\"Ship it!\\"}}"
      restartPolicy: Never
  backoffLimit: 2"""
  return template

def generate():
  with open('manifests/kuber-hook.yaml', 'w') as f:
    text = temp_file(f, sys.argv[1], sys.argv[2], sys.argv[3])
    f.write(text)

if __name__ == "__main__":
    generate()
