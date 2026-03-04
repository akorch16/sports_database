# 🚀 How to Publish Your Sports Database to GitHub Pages

## What You'll Get
- **Free hosting** for your sports database website
- **Automatic updates** every 6 hours (live data)
- **Custom domain** option (optional, paid)
- **No coding required** after setup

---

## Step 1: Create a GitHub Account (if you don't have one)
1. Go to **https://github.com/signup**
2. Sign up with your email
3. Verify your email
4. You're done! 🎉

---

## Step 2: Create a New Repository

1. Go to **https://github.com/new**
2. Fill in:
   - **Repository name:** `sports-database` (or any name you like)
   - **Description:** "Live sports records and rankings database"
   - **Visibility:** Select **Public** (required for free GitHub Pages)
   - **Initialize with README:** Check this box
3. Click **Create repository**

---

## Step 3: Upload Your Files

### Method A: Using GitHub Website (Easiest)

1. In your new repository, click **Add file** → **Upload files**
2. Drag and drop these files:
   - `sports_records.html`
   - `sports_records.db`
   - `database_to_html_extended.py`
3. Scroll down and click **Commit changes**

### Method B: Using Command Line (If you're comfortable with terminal)
```bash
git clone https://github.com/YOUR_USERNAME/sports-database.git
cd sports-database
cp /path/to/sports_records.html .
cp /path/to/sports_records.db .
cp /path/to/database_to_html_extended.py .
git add .
git commit -m "Add sports database files"
git push origin main
```

---

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll down to **Pages** section (left sidebar)
4. Under "Source":
   - Select branch: **main**
   - Select folder: **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes for deployment
7. You'll see a message: "Your site is published at `https://YOUR_USERNAME.github.io/sports-database`"

---

## Step 5: View Your Site

Your website is now live at:
```
https://YOUR_USERNAME.github.io/sports-database/sports_records.html
```

**Example:** If your GitHub username is `john-smith`, your URL would be:
```
https://john-smith.github.io/sports-database/sports_records.html
```

---

## Optional: Set Up Auto-Updates with GitHub Actions

To automatically fetch fresh data every 6 hours:

1. In your repository, create a folder: `.github/workflows/`
2. Create a file: `.github/workflows/update-sports-data.yml`
3. Copy this content:

```yaml
name: Update Sports Data

on:
  schedule:
    - cron: '0 */6 * * *'  # Runs every 6 hours
  workflow_dispatch:  # Allows manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
      
      - name: Run update script
        run: python database_to_html_extended.py
      
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Update sports data - $(date)" || true
          git push
```

4. Save and commit the file
5. GitHub will now automatically update your data every 6 hours! ✨

---

## Optional: Use a Custom Domain

To use your own domain (like `sports.yoursite.com`):

1. Buy a domain from **Namecheap**, **GoDaddy**, or **Google Domains**
2. In your GitHub repo → **Settings** → **Pages**
3. Under "Custom domain", enter your domain name
4. Configure your domain's DNS settings (GitHub provides instructions)

**Cost:** ~$12/year for a domain (hosting is still free)

---

## Troubleshooting

### "Site not showing up"
- Wait 2-3 minutes after enabling Pages
- Check that your repository is **Public**
- Make sure you selected the correct branch/folder in Pages settings

### "Can't find sports_records.html"
- Make sure the file is in the root directory of your repo
- File names are case-sensitive

### "Data not updating"
- Check your workflow file has correct syntax (YAML is picky with spacing)
- Go to **Actions** tab to see if workflows ran successfully

---

## Quick Reference: Your URLs

| File | URL |
|------|-----|
| HTML Dashboard | `https://USERNAME.github.io/sports-database/sports_records.html` |
| Database File | `https://USERNAME.github.io/sports-database/sports_records.db` |
| Python Script | `https://USERNAME.github.io/sports-database/database_to_html_extended.py` |

---

## Next Steps

1. ✅ Follow Steps 1-4 above
2. 📱 Share your link with friends!
3. 🔄 (Optional) Set up auto-updates with GitHub Actions
4. 🌐 (Optional) Get a custom domain

**That's it!** Your sports database is now published! 🎉

---

## Need More Help?

- **GitHub Pages Docs:** https://pages.github.com/
- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **Questions about the sports database?** Re-run the Python script anytime to regenerate the HTML

Happy publishing! 🏆
