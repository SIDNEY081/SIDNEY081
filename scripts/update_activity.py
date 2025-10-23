#!/usr/bin/env python3

import os
import requests
from datetime import datetime

def get_sidney_activity():
    """Get Sidney081's real GitHub activity"""
    # Using GitHub API to get real events
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    
    url = "https://api.github.com/users/Sidney081/events"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            events = response.json()
            
            activities = []
            for event in events[:6]:  # Get last 6 events
                if event['type'] == 'PushEvent':
                    repo = event['repo']['name']
                    commits = event['payload']['commits']
                    activities.append(f"🔨 Pushed {len(commits)} commit(s) to {repo}")
                elif event['type'] == 'CreateEvent':
                    repo = event['repo']['name']
                    activities.append(f"🎉 Created repository {repo}")
                elif event['type'] == 'IssuesEvent':
                    repo = event['repo']['name']
                    action = event['payload']['action']
                    activities.append(f"📝 {action} issue in {repo}")
                elif event['type'] == 'WatchEvent':
                    repo = event['repo']['name']
                    activities.append(f"⭐ Starred {repo}")
                elif event['type'] == 'ForkEvent':
                    repo = event['repo']['name']
                    activities.append(f"🍴 Forked {repo}")
                    
            return activities[:5] if activities else get_fallback_activities()
        else:
            print(f"API returned status: {response.status_code}")
            return get_fallback_activities()
                
    except Exception as e:
        print(f"Error fetching activity: {e}")
        return get_fallback_activities()

def get_fallback_activities():
    """Fallback activities that match YOUR known projects"""
    return [
        "🔨 Working on SafeShell Android app",
        "🧠 Developing AI-Stroke-Shield project",
        "🌐 Building portfolio website", 
        "📚 Studying Embedded Systems @ VUT",
        "⚡ Exploring IoT and AI technologies"
    ]

def update_readme():
    # Read current README
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Get real activity
    activities = get_sidney_activity()
    
    # Create activity section
    activity_content = "### ⚡ Recent Activity\n\n"
    for i, activity in enumerate(activities, 1):
        activity_content += f"{i}. {activity}\n"
    
    activity_content += f"\n_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n"
    
    # Update the activity section in README
    start_marker = "<!--START_SECTION:activity-->"
    end_marker = "<!--END_SECTION:activity-->"
    
    start_index = content.find(start_marker) + len(start_marker)
    end_index = content.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        new_content = content[:start_index] + "\n" + activity_content + "\n" + content[end_index:]
        
        # Write updated README
        with open('README.md', 'w') as f:
            f.write(new_content)
        print("✅ Successfully updated README with Sidney081's activity!")
    else:
        print("❌ Could not find activity markers in README")

if __name__ == '__main__':
    update_readme()
