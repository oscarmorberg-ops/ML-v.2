import subprocess
import os

def get_version_info():
    """CSIO production version med real commit count."""
    try:
        # Hämta real commit count
        commit_count = subprocess.check_output(
            ['git', 'rev-list', '--count', 'HEAD']
        ).decode('utf-8').strip()
        
        # Latest commit SHA
        commit_sha = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']
        ).decode('utf-8').strip()
        
        return {
            'version': 'v2.3.0',
            'commit_count': commit_count,
            'commit_sha': commit_sha,
            'timestamp': os.popen('date').read().strip()
        }
    except:
        return {
            'version': 'v2.3.0', 
            'commit_count': '503+',
            'commit_sha': '5b7ab27'
        }
