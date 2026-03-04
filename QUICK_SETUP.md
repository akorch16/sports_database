# ⚡ Quick Setup Checklist

## 5-Minute Setup (GitHub Pages)

### Step 1: Create GitHub Account
- [ ] Go to https://github.com/signup
- [ ] Sign up and verify email

### Step 2: Create Repository
- [ ] Go to https://github.com/new
- [ ] Name it: `sports-database`
- [ ] Make it **Public**
- [ ] Click **Create repository**

### Step 3: Upload Files
- [ ] Click **Add file** → **Upload files**
- [ ] Upload these 3 files:
  - [ ] `sports_records.html`
  - [ ] `sports_records.db`
  - [ ] `database_to_html_extended.py`
- [ ] Click **Commit changes**

### Step 4: Enable GitHub Pages
- [ ] Go to **Settings** → **Pages**
- [ ] Select branch: **main**
- [ ] Select folder: **/** (root)
- [ ] Click **Save**
- [ ] Wait 1-2 minutes

### Step 5: Visit Your Site
- [ ] Copy your URL: `https://USERNAME.github.io/sports-database/sports_records.html`
- [ ] Open it in your browser
- [ ] Share it with friends! 🎉

---

## Optional: Auto-Updates (10 minutes)

### Step 6: Set Up Automatic Data Refresh
- [ ] In your GitHub repo, create folder: `.github/workflows/`
- [ ] Create file: `update-sports-data.yml`
- [ ] Copy contents from `.github_workflows_update-sports-data.yml` file
- [ ] Commit the file
- [ ] Go to **Actions** tab to verify it's set up
- [ ] Data will auto-update every 6 hours! 🔄

---

## Optional: Custom Domain (15 minutes)

### Step 7: Buy a Domain (Optional)
- [ ] Visit: https://namecheap.com or https://domains.google
- [ ] Search for your desired domain
- [ ] Buy it (~$12/year)
- [ ] Note your domain name (e.g., `sports.yoursite.com`)

### Step 8: Connect Domain to GitHub Pages
- [ ] In your GitHub repo → **Settings** → **Pages**
- [ ] Under "Custom domain", enter your domain
- [ ] Follow GitHub's DNS instructions (varies by registrar)
- [ ] Your site is now at your custom domain! ✨

---

## Your Final URLs

Once deployed, you'll have:

**Default (Free) URL:**
```
https://YOUR_USERNAME.github.io/sports-database/sports_records.html
```

**Custom Domain (Optional, $12/year):**
```
https://yourdomain.com/sports_records.html
```

---

## Files You Have

| File | Purpose |
|------|---------|
| `sports_records.html` | Your website (upload to GitHub) |
| `sports_records.db` | Database with all sports data (upload to GitHub) |
| `database_to_html_extended.py` | Script to update HTML from database (upload to GitHub) |
| `DEPLOYMENT_GUIDE.md` | Full detailed instructions |
| `.github_workflows_update-sports-data.yml` | Auto-update configuration (create in GitHub) |

---

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| "Site not showing" | Wait 2-3 min, check repo is Public, verify Pages settings |
| "File not found (404)" | Check filename spelling/capitalization, ensure file is in root folder |
| "Data not updating" | Check Actions tab for errors, verify workflow YAML syntax |
| "Want custom domain" | Buy domain, add in Pages settings, update DNS |

---

## Support Resources

- 🆘 **GitHub Pages Help:** https://pages.github.com/
- 🤖 **GitHub Actions Help:** https://docs.github.com/en/actions
- 📚 **Full Guide:** See `DEPLOYMENT_GUIDE.md`

---

## Success! 🎉

Once live, you can:
- ✅ Share link with anyone
- ✅ Data updates automatically every 6 hours
- ✅ No monthly costs (free forever)
- ✅ No servers to manage
- ✅ Professional-looking sports database

**Enjoy your sports database!** 🏆
