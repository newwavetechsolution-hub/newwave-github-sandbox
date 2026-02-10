# Phase 0 — START HERE: Git & SSH Setup

Do this once per machine before pushing to GitHub.

## 0. Make sure Git is installed

In a terminal:

```bash
git --version
```

If this prints a version (for example, `git version 2.x.x`), you’re good.  
If not, install Git using your OS instructions (for Ubuntu: `sudo apt install git`).

---

## 1. Create or sign in to a GitHub account

1. Go to `https://github.com` in your browser.
2. Sign in or create a new account.

You’ll need this account for repository access and SSH keys.

---

## 2. Configure your Git identity

Tell Git who you are. In your terminal:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

You can verify:

```bash
git config --global user.name
git config --global user.email
```

---

## 3. Check if you already have an SSH key

List keys in `~/.ssh`:

```bash
ls ~/.ssh
```

If you see files like `id_ed25519` and `id_ed25519.pub`, you probably already have a usable key.  
Show the **public** key:

```bash
cat ~/.ssh/id_ed25519.pub
```

If that prints a long line starting with `ssh-ed25519`, you can skip to **Step 4**.

---

## 4. Generate a new SSH key (if needed)

If you don’t see `id_ed25519.pub`, create a new key pair:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

When prompted:

- **File location:** press Enter to accept the default (`/home/you/.ssh/id_ed25519`).
- **Passphrase:** optional but recommended; you can also press Enter twice for no passphrase.

Then show the **public** key:

```bash
cat ~/.ssh/id_ed25519.pub
```

You should see one long line starting with `ssh-ed25519`.

> **Important:** never share the file without `.pub` (`id_ed25519`).  
> Only the `.pub` file is safe to paste into GitHub.

---

## 5. Add your SSH key to GitHub

1. Copy the entire output of:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

   It should look like:

   ```text
   ssh-ed25519 AAAA...long-random-text... your-email@example.com
   ```

2. In your browser, while logged into GitHub:
   - Go to **Settings → SSH and GPG keys → New SSH key**.
   - **Title:** something like `laptop` or `dev-box`.
   - **Key:** paste the whole line from your terminal.
   - Click **Add SSH key**.

If you see “Key is invalid. You must supply a key in OpenSSH public key format”, check that:

- You copied from `id_ed25519.pub`, **not** `id_ed25519`.
- You copied **one whole line**, starting with `ssh-ed25519`, with no extra characters or prompts.

---

## 6. Test your SSH connection

Back in the terminal:

```bash
ssh -T git@github.com
```

The first time, you may be asked to confirm GitHub’s host key; type `yes` and press Enter.

If everything is set up correctly, you should see something like:

```text
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

At this point, SSH is working, and you can use URLs like:

```bash
git@github.com:your-username/your-repo.git
```

---

## 7. Optional: use HTTPS instead of SSH

If you prefer HTTPS (for example, for students who don’t want to manage SSH keys yet), you can set your remote like:

```bash
git remote set-url origin https://github.com/your-username/your-repo.git
```

Git will then prompt for GitHub credentials or use a credential helper.

