# Push Changes to GitHub

Repository: **https://github.com/mohamedmagdy482024-cloud/UI_sampel**

Git is already initialized and connected to this repository.

## Push Future Changes

After you edit files, run these commands from the project folder:

```powershell
cd "D:\New folder\UI_sampel-main"

git status
git add .
git commit -m "Describe your changes here"
git pull origin main --rebase
git push origin main
```

## Quick One-Line Push

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

## First-Time Setup (only if you clone on a new machine)

```powershell
git clone https://github.com/mohamedmagdy482024-cloud/UI_sampel.git
cd UI_sampel
```

Then use the **Push Future Changes** commands above.
