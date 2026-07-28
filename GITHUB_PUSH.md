# Push Changes to GitHub

Repository: **https://github.com/mohamedmagdy482024-cloud/UI_sampel**

## First-Time Setup (only once per machine)

If the project is not a git repository yet, run these commands from the project folder:

```powershell
cd "D:\New folder\UI_sampel-main"

git init
git remote add origin https://github.com/mohamedmagdy482024-cloud/UI_sampel.git
git fetch origin
git branch -M main
git reset origin/main
```

## Push Future Changes

After you edit files, use these commands every time you want to update GitHub:

```powershell
cd "D:\New folder\UI_sampel-main"

git status
git add .
git commit -m "Describe your changes here"
git pull origin main --rebase
git push origin main
```

## Quick One-Line Push (after setup)

```powershell
cd "D:\New folder\UI_sampel-main"; git add .; git commit -m "Update UI components"; git pull origin main --rebase; git push origin main
```

## Notes

- Replace the commit message with a short description of what you changed.
- If `git pull origin main --rebase` shows conflicts, fix the files, then run:

```powershell
git add .
git rebase --continue
git push origin main
```

- If GitHub asks for login, use your GitHub username and a **Personal Access Token** instead of your password.
