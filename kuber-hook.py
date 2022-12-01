import sys 

def temp_file(file, github_token, repo, run_id, env_id):
  template = f"""apiVersion: batch/v1
kind: Job
metadata:
  generateName: app-slack-notification-
  annotations:
    argocd.argoproj.io/hook: PostSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
spec:
  template:
    spec:
      containers:
      - name: slack-notification
        image: curlimages/curl
        command:
          - "curl"
          - "-X"
          - "POST"
          - "--data-urlencode"
          - "-H"
          - "Authorization: Bearer {github_token}"
          - "https://api.github.com/repos/PricerAB/{repo}/actions/runs/{run_id}/pending_deployments"
          - "-d" 
          - '{{"environment_ids":[{env_id}],"state":"approved","comment":"Ship it!"}}'
      restartPolicy: Never
  backoffLimit: 2"""
  return template

def generate():
  with open('manifests/kuber-hook.yaml', 'w') as f:
    text = temp_file(f, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    f.write(text)

if __name__ == "__main__":
    generate()