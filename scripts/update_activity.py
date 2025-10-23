#!/usr/bin/env python3

from datetime import datetime

def update_activity():
    # Read current README
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Create updated activity content
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_activity = f"""<!--START_SECTION:activity-->
🚀 **Sidney081 - Profile Active**

**Last Updated:** {timestamp}

📌 **Recent Activity:**
1. 🔨 Working on SafeShell Android app
2. 🧠 Developing AI-Stroke-Shield project  
3. 🏢 Enhancing MICTSETA Recruitment System
4. 📚 Learning Embedded Systems @ VUT
5. ⚡ Exploring IoT & AI technologies

💡 *This section updates automatically*
<!--END_SECTION:activity-->"""
    
    # Replace the activity section
    start_marker = "<!--START_SECTION:activity-->"
    end_marker = "<!--END_SECTION:activity-->"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        updated_content = content[:start_idx] + new_activity + content[end_idx:]
        
        # Write back to README
        with open('README.md', 'w') as f:
            f.write(updated_content)
        print("✅ README updated successfully!")
    else:
        print("❌ Could not find activity markers")

if __name__ == "__main__":
    update_activity()
