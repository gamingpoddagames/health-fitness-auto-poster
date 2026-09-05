# Health & Fitness Facebook Auto-Poster

## 🏋️ Completely Automated Facebook Content System

### Features
- ✅ **100% Free** - Runs on GitHub Actions
- ✅ **Fully Automatic** - Posts daily on schedule
- ✅ **No Copyright Issues** - Uses royalty-free content
- ✅ **Auto-Generates Content** - 50 posts ready to go
- ✅ **Supports Text, Images & Videos** 
- ✅ **No Setup Required** - Just add Facebook token

### Setup Instructions

1. **Fork this repository** to your GitHub account

2. **Get Facebook Page Access Token**:
   - Go to [Facebook Developers](https://developers.facebook.com/)
   - Create an App → Add "Facebook Login" product
   - Generate Page Access Token with these permissions:
     - `pages_manage_posts`
     - `pages_read_engagement`
     - `pages_manage_engagement`

3. **Add GitHub Secrets**:
   - Go to Settings → Secrets and variables → Actions
   - Add `FACEBOOK_PAGE_ID` (your numeric page ID)
   - Add `FACEBOOK_PAGE_ACCESS_TOKEN` (your long-lived token)

4. **Run It!**:
   - The system will post automatically at 8 AM, 1 PM, and 6 PM UTC
   - Or trigger manually from Actions tab → "Run workflow"

### Content Sources
- Text: Original health tips and motivational quotes
- Images: Lorem Picsum (royalty-free stock photos)
- Videos: Sample videos (public domain)

### Troubleshooting

- **"Missing credentials"** - Check GitHub Secrets
- **"Token expired"** - Generate new token (valid ~90 days)
- **"Video failed"** - System automatically falls back to text-only

### License
MIT - Free for personal and commercial use
