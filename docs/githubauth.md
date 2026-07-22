# GitHub Authentication: HTTPS → SSH

## Check the current remote

```bash
git remote -v
```

Example (HTTPS):

```text
origin  https://github.com/<username>/<repo>.git (fetch)
origin  https://github.com/<username>/<repo>.git (push)
```

---

## Change the remote from HTTPS to SSH

```bash
git remote set-url origin git@github.com:<username>/<repo>.git
```

Example:

```bash
git remote set-url origin git@github.com:nur/platform-engineering-journey.git
```

---

## Verify the change

```bash
git remote -v
```

Expected output:

```text
origin  git@github.com:<username>/<repo>.git (fetch)
origin  git@github.com:<username>/<repo>.git (push)
```

---

# Setting up SSH on a new machine

## 1. Generate an SSH key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press **Enter** to accept the default location.

---

## 2. Start the SSH agent

```bash
eval "$(ssh-agent -s)"
```

---

## 3. Add your SSH key

```bash
ssh-add ~/.ssh/id_ed25519
```

---

## 4. View your public key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output.

---

## 5. Add the key to GitHub

GitHub → **Settings** → **SSH and GPG keys** → **New SSH Key**

Paste the copied public key.

---

## 6. Test the connection

```bash
ssh -T git@github.com
```

Expected output:

```text
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

---

# Standard Git Workflow

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Your commit message"
```

Push:

```bash
git push
```

---

# Useful Reminder

- **HTTPS** uses a Personal Access Token (PAT), not your GitHub password.
- **SSH** uses your machine's SSH key.
- Every computer has its **own SSH key**.
- Your Ubuntu server's SSH key does **not** automatically work on your Windows machine.
